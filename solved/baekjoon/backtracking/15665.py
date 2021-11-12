n, m = map(int, input().split()) #O(2)
arr = list(map(int, input().split())) #O(7log7)
arr.sort() #O(7log7)
visited = dict()

def recurse(result, trial):
    if trial == m+1:#O(3)
        print(" ".join(map(str, result))) #O(16)
        return
    for i in arr:
        result.append(i) #O(1)
        tmp = tuple(result) #O(7)
        if not visited.get(tmp): #O(1)
            visited[tmp]=True#O(1)
            recurse(result, trial+1) #O(1)
        result.pop() #O(1)
    return

recurse([], 1)