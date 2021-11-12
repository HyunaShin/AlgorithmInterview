n,m = map(int, input().split())
numbers = [int(i) for i in input().split()]
numbers.sort()

def dfs(result, depth):
    #O(N!)
    if depth == m+1:
        print(" ".join(result))
        return
    for num in numbers:
        if result and str(num) in result:
            continue
        dfs(result + [str(num)], depth +1)
    return
dfs([], 1)