n,m = map(int, input().split())
numbers = [int(i) for i in input().split()]
numbers.sort()

def dfs(result):
    #O(N!)
    if len(result) == m:
        print(" ".join(result))
        return
    for num in numbers:
        if result and str(num) in result:
            continue
        dfs(result + [str(num)])
    return
dfs([])