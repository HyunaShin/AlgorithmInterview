from collections import deque

def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    while queue:
        print(queue)
        virus, _s, _x, _y = queue.popleft()
        #왜 이때 멈출까?
        #큐에 넣을때 0초인 부분 소진 완료, 1초인 부분 append-pop 완료 이후 2초인 부분에 대해 append-pop이 된다.
        #이 때 그 다음 이터레이션상 3초에 대해 넣게 되는데, 이 때 2초에 대한 부분은 다
        if _s == s:
            break

        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                graph[nx][ny] = virus
                queue.append((virus, _s+1, nx, ny))


if __name__ == "__main__":
    n,k = list(map(int, input().split(" ")))
    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split(" "))))

    s,x,y = list(map(int, input().split(" ")))

    queue = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                queue.append((graph[i][j], 0, i, j ))

    res = bfs()
    print(graph[x-1][y-1])

