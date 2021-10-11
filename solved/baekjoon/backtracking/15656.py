n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def dfs(result, trial):
    if trial == m+1:
        print(" ".join(map(str, result)))
        return
    for val in arr:
        dfs(result + [val], trial+1)
    return

dfs([],1)