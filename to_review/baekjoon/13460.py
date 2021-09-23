import copy


def solution():
    from sys import stdin
    from collections import deque

    input = stdin.readline
    n,m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    #차원이 늘어나기도 하고, 대부분이 False일테지만!
    # rx, ry, bx, by의 좌표를 표현할 수 있고
    # rx, ry, bx, by가 방문 헀는지 체크하는게 목표니까, 있는 걸 없다그러진 않잖아? 노프라블럼
    visited = [[[[False] *m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    dx, dy = (-1,0,1,0), (0,1,0,-1)
    q = deque()
    def init():
        rx, ry, bx, by = [0] * 4 #초기화 0,0,0,0
        for i in range(n):
            for j in range(m):
                #board에 빨간 구슬이라면 좌표값 저장
                if board[i][j] == "R":
                    rx, ry = i,j
                #board에 파란 구슬이라면 좌표값 저장
                elif board[i][j] == "B":
                    bx, by = i,j
        #위치 정보와 움직인 횟수
        # 종료 조건으로 0을 걸어 줄거라, 1 추가하고 시작
        q.append((rx, ry, bx, by, 1))
        visited[rx][ry][bx][by] = True

    def move(x, y, dx, dy):
        #이동한 칸 수
        count = 0
        #다음 이동이 벽이거나 구멍이 아닐 떄까지
        while board[x+dx][y+dy] != "#" and board[x][y] != "O":
            x += dx
            y += dy
            count +=1
        return x,y, count

    def bfs():
        init()
        while q:
            rx, ry, bx, by, depth = q.popleft()
            if depth > 10:
                #제약 조건 : 움직인 횟수는 10 이하여야한다.
                break
            #규칙 : 상,하,좌우로 움직인다.
            for i in range(4):
                nrx, nry, r_cnt = move(rx, ry, dx[i], dy[i])
                nbx, nby, b_cnt = move(bx, by, dx[i], dy[i])

                #탐색 중지 조건 : 어떤 케이스든 파란구슬이 구멍에 떨어지면 안댐
                if board[nbx][nby] == "O":
                    continue
                #탐색 종료 조건 : 빨간 구슬이 구멍에 떨어지면 성공
                if board[nrx][nry] == "O":
                    # print(depth)
                    return depth
                #제약 조건 : 빨간구슬과 파란구슬이 동시에 같은 같에 있을 수 없다.
                if nrx == nbx and nry == nby :
                    #이동거리가 많은 구슬을 한칸 뒤로
                    # -> 더 늦게 도착한 녀석이 더 뒤에 있어야 함
                    if r_cnt > b_cnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                #그럼 이런 제약, 종료 조건에 안걸리고 칸을 이동했다면
                #방문 처리를 해 준다.
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    #방문처리 이후, 큐에 탐색 시작점인 노드를 넣어줌
                    q.append((nrx, nry, nbx, nby, depth +1))
        return -1
    return bfs()

def maaaaaain():
    from collections import deque
    n,m = map(int,input().split())
    graph = [list(input().strip()) for _ in range(n)]
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    dx, dy = (1,-1,0,0), (0,0,1,-1)
    q = deque()
    def init():
        rx, ry, bx, by = [0] * 4  # 초기화 0,0,0,0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == "R":
                    rx = i
                    ry = j
                elif graph[i][j] == "B":
                    bx = i
                    by = j
        q.append((rx,ry,bx,by,1))
        visited[rx][ry][bx][by] = True

    def move(x, y, dx, dy):
        #이동한 칸 수
        cnt = 0
        while True:
            nx, ny = x + dx, y + dy
            #칸을 직선으로 한칸씩 옮기는 조건에 대한 구현이다.
            #앞에 벽이 있거나, 지금 구멍이면 더 못가지?
            if graph[nx][ny] != "#" and graph[x][y] != "O":
                x = nx
                y = ny
                cnt +=1
            else:
                return x, y, cnt

    def bfs():
        #큐에 방문 시작노드를 넣고 방문처리
        init()
        while q:
            rx,ry,bx,by,cnt = q.popleft()
            if cnt > 10:
                return -1
            for i in range(4):
                nrx, nry, r_cnt = move(rx,ry,dx[i],dy[i])
                nbx, nby, b_cnt = move(bx,by,dx[i],dy[i])

                if graph[nbx][nby] == "O":
                    continue

                elif graph[nrx][nry] == "O":
                    return cnt

                if nbx == nrx and nby == nry:
                    if r_cnt > b_cnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, cnt+1))

        return -1
    return bfs()

if __name__ == "__main__":
    ret = maaaaaain()
    print(ret)
