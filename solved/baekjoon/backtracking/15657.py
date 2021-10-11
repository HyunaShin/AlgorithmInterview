
def recurse(result, trial):
    if trial == m+1:
        print(" ".join(map(str, result)))
        return
    for v in arr:
        if result and result[-1] > v:
            continue
        recurse(result + [v], trial+1)
    return

def back_tracking(trial):
    if trial == m+1:
        print(" ".join(map(str, result)))
        return
    for idx in range(n):
        # if visited[idx] == False:
        if result and result[-1] > arr[idx]:
            continue
        #방문은 이제 체크 안해도됨(중복해야하니까)
        # visited[idx] = True
        result.append(arr[idx])
        back_tracking(trial+1)
        result.pop()
        # visited[idx]=False
    return


if __name__ == "__main__":
    n,m = map(int,input().split())
    arr = sorted(list(map(int, input().split())))

    # recurse([], 1)
    #arr의 인덱스와 visited의 인덱스는 동일하다
    visited=[False] * n
    result = []
    back_tracking(1)


