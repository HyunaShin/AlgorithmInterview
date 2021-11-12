n, m = map(int, input().split())
result = []
visited = [False] * (n+1)
def dfs(depth, n,m):
    #맨 마지막 스텝에서는
    if depth == m+1:
        #어떠한 행동을 하세요
        for i in range(0, len(result)):
            print(result[i], end=" ")
        print()
    return
    #이터레이션을 돌면서
    for num in range(1, N+1):
        #일전에 선택한 스텝이 아니면
        if not visited[num]:
            # 해당 이터레이션에 대해 방문처리를 한다.
            visited[num]=True
            # 한스텝 가보고
            result.append(num)
            #재귀적으로 일전에 선택한 스텝에 대해 들어가보고
            dfs(depth+1, n,m)
            #해당 스텝에서 엔딩을 봤으면, 다른 스텝으로 넘어가라
            result.pop()
            visited[num]=False

