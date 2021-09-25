def main():
    from collections import deque

    n,m = map(int, input().split())
    r,c,d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    turn = {0:3, 3:2, 2:1, 1:0 }
    #회전한 칸
    t =[False] * 4
    # t[d] = True
    q = deque()
    # q.append((r,c,d,t))
    q.append((r,c,d))
    graph[r][c] = 2

    while q:
        x,y,d = q.popleft()

        # # 바라보는 방향에서 그대로 한칸 후진
        bx, by = x - dx[d], y - dy[d]
        #왼쪽으로 회전했을때의 방향
        nd = turn[d]
        # 회전하고 직진하면
        nx, ny = x + dx[nd], y + dy[nd]

        #2-c
        #왼쪽에 청소할 공간이 없고, 네 방향 모두 봤다
        if sum(t) == 4:
            #뒤쪽이 벽이라 후진도 못한다.
            if graph[bx][by] == 1:
                #멈춘다.
                break
            #뒤쪽이 벽은 아니다 -> 차례대로 인접한 칸을 탐색한다.
            else:
                #바라보는 방향을 유지하고, 한칸 후진한다.
                q.append((bx, by, d, t))

        # a
        if 0<=nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            #그방향으로 회전, 전진
            # t[nd] = True
            q.append((nx, ny, nd))
            #현재 위치 청소 ->?
            graph[nx][ny] = 2

        #2-b
        #왼쪽에 청소할 공간이 없다, 네 방향 모두 보기 이전이다.
        elif graph[nx][ny] !=0: #and t < 4:
            #그 방향으로 회전하고, 왼쪽부터 인접한 칸 탐색 시행
            t[nd] = True
            q.append((x, y, nd, t))


    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                result +=1
    print(result)
    from pprint import pprint
    pprint(graph)
    return

def solution():
    from collections import deque
    n,m = map(int, input().split())
    r,c,d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [-1,0,1,0], [0,1,0,-1]

    #0 북 1동 2남 3서
    q = deque()
    q.append((r,c,d,2)) #r c d 청소 카운트(1이면 벽이랑 똑같아지니 노노)
    ans = 0
    while q:
        x,y, _d, count = q.popleft()
        next_d = _d
        flag = False
        if board[x][y] == 0:
            board[x][y] = count
        for _ in range(4):
            #방향 돌리는거
            next_d = (next_d-1) %4
            nx = x + dx[next_d]
            ny = y + dy[next_d]
            if board[nx][ny] == 0:
                q.append((nx, ny, next_d, count +1))
                flag = True
                break
        if not flag:
            backward_dir = (_d -2) %4
            bx = x + dx[backward_dir]
            by = y + dy[backward_dir]
            if board[bx][by] !=1:
                q.append((bx,by,_d,count))
        ans = count -1
    print(ans)
    # return ans

if __name__ == "__main__":
    solution()