n,m = map(int,input().split())
result = []
visited= [False] * (n+1) #노드의 방문 정보

def back_tracking():
    if len(result) == m:
        print(" ".join(result))
        return None

    #1부터 n 중에서
    for i in range(1, n+1):
        if visited[i] == False:
            #방문처리
            visited[i] = True
            #한스텝 갔다
            result.append(str(i))
            back_tracking()
            #엔딩까지 다 봤으면 돌아오기
            result.pop()
            visited[i] = False
    return

back_tracking()