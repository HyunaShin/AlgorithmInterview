n,m = map(int, input().split())
tmp = n+1
visited=[False] * (tmp)
result = []

def back_tracking(start_idx):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    for i in range(start_idx, tmp):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            back_tracking(i+1)
            result.pop()
            visited[i] = False
    return

back_tracking(1)
