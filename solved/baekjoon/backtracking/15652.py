
n,m = map(int, input().split())
result = []
def dfs(result):
    #제일 효율적인 소스(백트래킹이긴함)
    if len(result) == m:
        print(" ".join(result))
        #리턴값이 없으니, m까지 오면 result array는 이전 상태 트리에 있는 값들만.
        return

    for i in range(1,n+1):
        # 건너뛸 조건만 넣어주면 소스가 심플해짐
        if result and i < int(result[-1]):
            continue
        #지금까지의 상태 트리에 있는 값만 메모리에 올려둠
        dfs(result + [str(i)])

dfs(result)