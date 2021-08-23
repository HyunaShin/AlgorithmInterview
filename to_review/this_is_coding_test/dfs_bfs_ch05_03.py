# -*- coding:utf8 -*-
from collections import deque

def main(x,y):
    #재귀함수의 종료 조건
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        print(x,y)
        graph[x][y] = 1
        main(x, y-1)
        main(x, y+1)
        main(x+1, y)
        main(x-1, y)
        return True
    return False


def solution():
    n,m = map(int, input().split())

    graph =[]
    for i in range(n):
        graph.append(list(map(int, input())))

    def dfs(x,y):
        # 주어진 범위를 벗어나면 즉시 종료
        if x<=-1 or x >=n or y <= -1 or y >=m:
            return False

        #현재 노드를 아직 방문하지 않았으면
        if graph[x][y] == 0:
            #방문처리
            graph[x][y] = 1
            #상하좌우도 재귀적으로 호출
            dfs(x-1, y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
            return True
        return False

    #모든 위치에 대해 음료수 채우기
    result = 0
    for i in range(n):
        for j in range(m):
            #현재 위치에서 DFS 수행
            if dfs(i, j) == True:
                result +=1

    return result

if __name__ == "__main__":
    n,m = list(map(int, input().split(" ")))
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    result = 0
    for i in range(n):
        for j in range(m):
            result += main(i,j)

    solution()