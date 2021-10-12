n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited= [False] * n
resulted = dict()

def back_tracking(result, trial):
    if trial == m+1:
        tmp = " ".join(map(str, result))
        #똑같은 수열 또 출력하지 말고
        if resulted.get(tmp):
            return
        print(tmp)
        resulted[tmp]=True
        return

    for idx in range(n):
        #같은 인덱스 여러번 고르지 말고
        if visited[idx] == False:
            visited[idx] = True
            back_tracking(result + [arr[idx]], trial+1)
            visited[idx]=False

back_tracking([],1)