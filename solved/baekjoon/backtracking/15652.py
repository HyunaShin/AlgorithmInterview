n,m = map(int, input().split())
result = []
visited= set()
def dfs(result):
    if len(result) == m :
        print(" ".join(map(str, result)))
        return result

    for i in range(1, n+1):
        if len(result):
            if result[-1] <= i:
                result.append(i)
                result = dfs(result)
                if tuple(result) not in visited:
                    visited.add(tuple(result))
                result.pop()
        else:
            result.append(i)
            result = dfs(result)
            if tuple(result) not in visited:
                visited.add(tuple(result))
            result.pop()
    return result
dfs(result)