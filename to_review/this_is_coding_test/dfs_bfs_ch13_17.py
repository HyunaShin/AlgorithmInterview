from collections import deque

def bfs():
    '''
    큐에는 0초에서의 바이러스 정보가 바이러스 번호 순 대로 들어있다.
    따라서 0초 -> 1초 -> 2초로 늘어나는 상황에 대한 구현이 가능하다.
    큐에 뭘 넣어야할지에 대한 아이디어가 주요해 보인다.
    '''
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        #바이러스 종류, 시간, 위치
        virus,s,x,y = q.popleft()
        if s == target_s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #해당 위치로 이동할 수 있는 경우
            if 0 <= nx and nx < n and 0 <= ny and ny < n :
                #아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
                if graph[nx][ny] ==0:
                    graph[nx][ny] = virus
                    q.append((virus, s+1, nx, ny))

if __name__ == "__main__":
    n,k = list(map(int, input().split(" ")))
    graph = [] #전체 보드 정보를 담는 리스트
    data = [] #바이러스에 대한 정보를 담는 리스트
    for i in range(n):
        #보드를 한줄 단위로 입력
        graph.append(list(map(int, input().split(" "))))
        #해당 위치에 바이러스가 존재하는 경우
        for j in range(n):
            if graph[i][j] != 0:
                #(바이러스 종류, 시간, 위치 X, 위치 Y 삽입)
                data.append((graph[i][j], 0, i, j))

    #정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
    data.sort()
    q = deque(data)
    target_s,target_x,target_y = list(map(int, input().split(" ")))

    bfs()
    print(graph[target_x-1][target_y-1])