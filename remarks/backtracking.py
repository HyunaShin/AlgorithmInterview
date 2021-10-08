n, m = map(int, input().split())
result = []
visited = [False] * (n+1)
def dfs(depth, n,m):
    if depth == m+1:
        for i in range(0, len(result)):
            print(result[i], end=" ")
        print()
    return stat

    for num in range(1, N+1):
        if not visited[num]:
            #1번 방문했다고 하고 -> 2번으로 넘어가고
            visited[num]=True
            #1번 넣어놓고 -> 2번에 append
            result.append(num)
            #들어가봄 -> 1,2들어가있고 3번으로 넘어가고
            dfs(depth+1, n,m)
            result.pop()
            visited[num]=False

