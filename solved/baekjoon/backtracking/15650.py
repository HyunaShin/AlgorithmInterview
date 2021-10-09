n,m = map(int, input().split())
visited=[False] * (n+1)
result = []

def back_tracking(start_idx):
    if len(result) == m:
        #여기는 이터레이션 +1인 케이스
        #되는 이유는 배열의 길이로 봐서
        print(" ".join(result))
        return
    for i in range(start_idx, n+1):
        if visited[i] == False:
            if len(result):
                if int(result[-1]) < i:
                    visited[i] = True
                    result.append(str(i))
                    back_tracking(start_idx + 1)
                    result.pop()
                    visited[i] = False
            else:
                visited[i] = True
                result.append(str(i))
                back_tracking(start_idx + 1)
                result.pop()
                visited[i] = False
    return

back_tracking(1)
