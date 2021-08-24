# -*- coding:utf8 -*-

#깊이 우선 탐색으로 각 바이러스가 사방으로 퍼지게 하기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #상하좌우중 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                #해당 위치에 바이러스를 배치하고, 다시 재귀적으로 수행한다.
                temp[nx][ny] = 2
                virus(nx, ny)


# 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score +=1
    return score

def dfs(count):
    global result
    #울타리가 3개 설치된 경우
    if count == 3:
        # 나머지는 원래 맵에 있던값 그대로 쓰기
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        #바이러스 전파 시키기
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        #안전 영역의 최댓값 계산
        result = max(result, get_score())
        return None

    #======= 직접 전개 해 보면서 이해할 것 =======
    #빈공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count +=1
                dfs(count)
                data[i][j] = 0
                count -=1
    #======= 직접 전개 해 보면서 이해할 것 =======

if __name__ == "__main__":
    n, m = map(int, input().split())
    data = [] #초기 맵 리스트
    temp = [[0] * m for _ in range(n)] #벽을 설치하고 난 뒤의 맵 리스트

    for _ in range(n):
        data.append(list(map(int, input().split())))

    #4가지 이동 방향에 대한 리스트
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = 0
    dfs(0)
    print(result)
