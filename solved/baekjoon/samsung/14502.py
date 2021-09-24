from itertools import combinations
from collections import deque
import copy

n,m = map(int, input().split())
graph = []
wc = []
virus_loc = []
dx, dy = [0,1,-1,0], [-1,0,0,1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            virus_loc.append((i,j))
        if graph[i][j] == 0 :
            wc.append((i, j))

def bfs(x,y):
    global g_tmp
    q = deque()
    q.append((x,y))
    g_tmp[x][y] = 2
    while q:
        x,y = q.popleft()
        #바이러스가 있으면, 상하좌우로 퍼뜨린다.
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            #가려는 위치가 그래프 내이고, 빈칸이면
            if 0 <= nx < n and 0 <= ny < m and g_tmp[nx][ny] == 0:
                #감염시킨다.(방문 처리)
                g_tmp[nx][ny] = 2
                # 다음에 루트가 될 바이러스 위치
                q.append((nx, ny))

sz = 0
#벽을 만들 수 있는 경우의 수대로
for walls in combinations(wc,3):
    g_tmp = copy.deepcopy(graph)
    #벽을 세우고
    for w in walls:
        g_tmp[w[0]][w[1]] = 1
    #감염시키기
    for v in virus_loc:
        bfs(v[0],v[1])
    #다 감염 됐으면, 안전 영역의 크기를 센다.
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g_tmp[i][j] == 0:
                cnt +=1
    sz = max(sz, cnt)
print(sz)