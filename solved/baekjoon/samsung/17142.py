from collections import deque
from itertools import combinations
import copy

n,m = map(int, input().split())
board = []
visited = [[int(1e9)] * n for _ in range(n)]
virus_loc = []
dx,dy = [1,-1,0,0], [0,0,-1,1]
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 1:
            visited[i][j] = -int(1e9)
        elif board[i][j] == 2:
            visited[i][j] = -1
            virus_loc.append((i,j))

def bfs(x,y, visited, time):
    q = deque()
    q.append(((x,y), (visited, time)))
    visited[x][y] = 0
    while q:
        (x,y), (visited, time) = q.popleft()
        dt = time +1
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 :
                    visited[nx][ny] = 0
                    #비활성이 활성으로 바뀐다. 시간만 기록
                    q.append(((nx, ny), (visited, dt)))
                elif visited[nx][ny] != -int(1e9) and (visited[nx][ny]== int(1e9) or visited[nx][ny]>dt) :
                    visited[nx][ny] = dt
                    q.append(((nx,ny), (visited,dt)))

    return visited

min_time = int(1e9)
for v_case in combinations(virus_loc, m):#O(50**2C10)
    v_result = copy.deepcopy(visited)
    for v in v_case:#O(10)
        v_result = bfs(v[0], v[1], v_result, 0)  #O((50**2) *2 --> O(5000))

    time = 0
    for i in range(n):
        time = max(time, max(v_result[i]))
    min_time = min(time, min_time)

if min_time == int(1e9):
    print(-1)
else:
    print(min_time)
