n, m = map(int, input().split()) #O(2)
arr = list(map(int, input().split())) #O(7log7)
arr.sort() #O(7log7)
visited = dict()

def recurse(result, trial):
    if trial == m+1:
        print(" ".join(map(str, result))) #O(16)
        return
    for i in arr:
        tmp = result + (i,)
        if not visited.get(tmp):
            visited[tmp]=True
            recurse(tmp, trial+1)
    return

recurse((), 1)