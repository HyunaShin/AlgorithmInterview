def main():
    # from collections import deque
    #
    # n = int(input())
    # k = int(input())
    # #탐색할 그래프 초기화
    # visited = [[0] * n for _ in range(n)]
    # #사과가 있는 부분은 2로 표기
    # for _ in range(k):
    #     a,b = map(int, input().split())
    #     visited[a][b] = 2
    #
    # l = int(input())
    # turn = []
    # for _ in range(l):
    #     a,b = input().split(" ")
    #     turn.append((int(a), b))
    #
    # d = [(0,1), (1,0), (0,-1), (-1,0)]
    # l = [(0,1), (-1,0), (0,1), (1,0)]
    #
    # q = deque()
    #
    # q.append(([(0,0)],0))
    # visited[0][0] = 1
    # time = 1
    #
    # while q:
    #     snake, turn_cnt = q.popleft()
    #     steps, direction = turn.pop(0)
    #     if direction == "D":
    #         turn_cnt +=1
    #         dx, dy = d[turn_cnt%4]
    #     else:
    #         turn_cnt +=1
    #         dx, dy = l[turn_cnt%4]
    #
    #     while steps: #3번동안
    #         for i in range(len(snake)): #뱀 몸통 옮기기
    #             x,y = snake[i] #뱀 토막
    #             nx, ny = x+dx, y+dy #옮길 위치
    #             if 0 <= nx < n and 0 <= ny < n: #옮길 위치가 그래프 내라면
    #                 if visited[nx][ny] == 0: #방문 안했으면 방문하기
    #                     visited[nx][ny] = 1
    #                     visited[x][y] = 0 #이전에 있던 칸은 0으로
    #                     snake[i] = (nx,ny)
    #                 elif visited[nx][ny] == 2: #사과라면
    #                     visited[nx][ny] = 1 #방문했다고하기, 뱀 위치 업데이트
    #                     snake = [(nx,ny)] + snake[1:]
    #                 else:
    #                     #그래프 내이고, 이미 방문했으면 몸통이랑 부딪힌거다
    #                     return time
    #             else:
    #                 #그래프 밖이면 벽에 부딪힌거다.
    #                 return time
    #         #움직일 칸 수 빼기
    #         steps -=1
    #         #1초 지남
    #         time +=1
    #     # ([뱀이 차지하는 칸],direcion cnt
    #     q.append((snake,turn_cnt))
    from collections import deque
    n = int(input())
    k = int(input())
    graph = [[0] * n for _ in range(n)]
    #사과가 있으면 2로 표기
    for _ in range(k):
        a,b = map(int, input().split())
        graph[a][b] = 2
    time_direction = dict()
    l = int(input())
    for _ in range(l):
        a, b = input().split()
        time_direction[int(a)] = b

    def run():
        x, y = 0, 0
        direction = 1
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        q = deque([[x, y]])
        time = 1
        while True:
            x,y = x + dx[direction], y + dy[direction]
            if 0<= x < n and 0 <= y < n and graph[x][y] !=1:
                #사과가 없다면
                if graph[x][y] != 1:
                    tmp_x, tmp_y = q.popleft()
                    #몸 길이를 줄여서 꼬리가 위치한 칸 비우기
                    graph[tmp_x][tmp_y] = 0
                #그럼 머리가 앞으로 가야지
                #사과가 있으면 머리가 가고, 없으면 꼬리 줄여서 가고
                graph[x][y] = 1
                q.append([x,y])
                #잎으로 갔으면, 틀지말지 결정
                if time in time_direction.keys():
                    if time_direction[time] == "D":
                        direction = (direction+1)%4
                    else:
                        direction = (direction-1)%4
                #틀기까지 다했으면, 시간 추가
                time +=1
            else:
                return time
    print(run())


def solution():

    from collections import deque
    def change(d,c):
        # d : 지금 위치, c: L/D  틀어야 하는 방향
        #상(0), 우(1) 하(2), 좌(3)
        #동쪽 회전 : 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0): +1방향
        #왼쪽 회전 : 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1방향
        if c == "L":
            d = (d-1) %4
        else:
            d = (d+1) %4
        return d

    def start():
        direction = 1 #초기 방향
        time = 1 #시간
        y,x = 0,0 #초기 뱀 위치
        #3. (0,0)에서 뱀은 시작하며 뱀이 지나갔던 곳은 2로 저장한다.
        visited=deque([[y,x]])
        arr[y][x] = 2
        while True:
            #방향의 변화가 생겼는지 확인한다.(direction : 방향)
            y,x = y + dy[direction], x + dx[direction]
            #그래프 범위 안이고, 방문 안했으면
            if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
                # 사과가 없는 경우, 원래 있던 칸을 비워줘야함
                if not arr[y][x] == 1:
                    #방문한 칸에서 원래 있던 위치 빼오고
                    temp_y, temp_x = visited.popleft()
                    #꼬리 제거
                    arr[temp_y][temp_x] = 0
                #이동하려는 칸 방문
                arr[y][x] = 2
                #머리 업데이트(제일 오른쪽이 머리, 제일 앞쪽이 꼬리)
                visited.append([y,x])
                # 지금 틀어야하는 시간이라면
                if time in times.keys():
                    #방향 틀어조라
                    direction = change(direction, times[time])
                #그럼 1초 지남
                time +=1
            else:
                #벽에 부딪히거나, 몸통에 부딪혔다면 걸린 시간 뱉아내기
                return time

    N = int(input())
    k = int(input())
    #1. 2차원 배열을 만든다.
    arr = [[0] * N for _ in range(N)]
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    #사과의 위치에 1을 저장한다.
    for _ in range(k):
        a,b = map(int, input().split())
        arr[a-1][b-1] = 1
    L = int(input())
    times = {}
    for i in range(L):
        X,C = input().split()
        #몇초 뒤에 회전할지
        times[int(X)] = C
    print(start())


if __name__ == "__main__":
    res = main()
    print(res)
