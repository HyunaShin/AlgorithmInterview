n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = dict()
def recurse(result, idx, trial):
    if trial == m+1:
        print( " ".join(map(str, result)))
        return
    for i in range(idx, n):
        tmp = result + (arr[i],)
        if not visited.get(tmp):
            visited[tmp]=True
            recurse(tmp, i+1, trial+1)

recurse(tuple([]), 0, 1)