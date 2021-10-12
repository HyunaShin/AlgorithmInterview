n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited= dict()
def back_tracking(result,idx,trial):
    if trial == m+1: #O(3)
        print(" ".join(map(str, result))) #O(16)
        return

    for i in range(idx, n):
        result.append(arr[i]) #O(1)
        tmp = tuple(result) #O(8)
        if not visited.get(tuple(tmp)): #O(1+1+8)
            visited[tmp]=True #O(1)
            back_tracking(result, i, trial+1) #O(1)
        result.pop() #O(1)

back_tracking([], 0,1)