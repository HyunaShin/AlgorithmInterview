# -*- coding:utf8 -*-
from collections import deque
def main(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] +1

            else:
                continue
    return graph[n-1][m-1]



def solution(x,y):
    #이동할 방향
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 밖을 벗어난 경우 무시
            if nx <0 or ny <0 or nx >= n or ny >= m:
                continue

            #벽 무시
            if graph[nx][ny] == 0:
                continue

            #해당 노드 처음 방문ㅇ시에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))

    return graph[n-1][m-1]


if __name__ == "__main__":
    n,m = list(map(int, input().split(" ")))
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    x,y = 0,0
    ret = main(x,y)

    # ret = solution(x,y)
    print(ret)