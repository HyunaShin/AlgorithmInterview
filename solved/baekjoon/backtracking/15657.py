n,m = map(int,input().split())
arr = sorted(list(map(int, input().split())))
def recurse(result, trial):
    if trial == m+1:
        print(" ".join(map(str, result)))
        return
    for v in arr:
        if result and result[-1] > v:
            continue
        recurse(result + [v], trial+1)
    return

recurse([], 1)

