n = int(input())
#그래프
graph = [list(map(int, input().split())) for _ in range(n)]
#합쳐진 정보
merged = [[False] * n  for _ in range(n)]
visited = [[False] * n  for _ in range(n)]
dx, dy = (1,-1,0,0),(0,0,1,-1)

def move(graph, visited, merged, dx, dy, cnt):
    if cnt == 5:
        max_num = 0
        #N^2 +3
        for i in range(n): #N
            for j in range(n): #N
                max_num = max(max_num, graph[i][j]) #3
                merged[i][j] = False
        return max_num, graph
    run_state =1
    while run_state:
        # print(run_state)
        for x in range(n):
            for y in range(n):
                nx, ny = x + dx, y + dy
                visited[x][y] = True
                #가려는 위치가 그래프 범위 내라면
                if 0<= nx < n and 0 <= ny < n:
                    #두개가 같고, 합쳐진 이력이 없다면
                    if graph[nx][ny] == graph[x][y] and merged[nx][ny] == False:
                        #밀고
                        graph[nx][ny] += graph[x][y]
                        #원래칸은 빈칸으로
                        graph[x][y] = 0
                        merged[nx][ny] = True
                    #두개가 다르다면
                    if graph[nx][ny] != graph[x][y]:
                        #0인 경우 앞으로 한칸씩 오자, 아닌경우는 몬움직인ㄴ다
                        if graph[nx][ny] == 0:
                            graph[nx][ny] = graph[x][y]
                            graph[x][y] = 0
        run_state = n*n
        for x in range(n):
            run_state -= sum(visited[x])

    max_num = 0
    for _ in range(4):
        _max, graph = move(graph, visited, merged, dx, dy, cnt + 1)
        max_num = max(max_num,_max)
    return max_num, graph

max_num = 0
for i in range(4):
    _max, graph = move(graph, visited, merged, dx[i], dy[i], 1)
    max_num = max(max_num,_max)
    if max_num == _max:
        print(graph)
# print(graph)
print(max_num)