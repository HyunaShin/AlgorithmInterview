# -*- coding:utf8 -*-
from itertools import combinations
from collections import deque

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    dx = [-1,1,0,0]
    dy = [0,0,1,1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx, ny)
            if nx < 0 or nx > n-1 or ny< 0 or ny > m-1:
                continue

            if graph[nx][ny] == 0 :
                queue.append((nx, ny))
                graph[nx][ny] = 2

    return graph

def main(wall_candidates):
    tmp_graph = graph
    max_safe_zone = -1
    #경우의 수대로 벽을 세우고
    for walls in combinations(wall_candidates, 3):
        #벽세우기
        for wall in walls:
            tmp_graph[wall[0]][wall[1]] = 1

        #바이러스 감염시키기
        for virus in viruses:
            tmp_graph = bfs(tmp_graph, virus)
            # if set(walls) == {(1,6), (2,5), (2,6)}:
            #     for i in range(n):
            #         print(tmp_graph[i])
            #         print()


        #안전구역 세기
        tmp_safe_zone=0
        for i in range(n):
            for j in range(m):
                if tmp_graph[i][j] == 0:
                    tmp_safe_zone +=1

        max_safe_zone = max(tmp_safe_zone, max_safe_zone)
        tmp_graph = graph

    return max_safe_zone

if __name__ == "__main__":
    n,m = list(map(int, input().split(" ")))
    graph = []
    wall_candidates = []
    #바이러스가 있는 구간 마다 bfs실시
    viruses = []
    for i in range(n):
        val = list(map(int, input().split(" ")))
        graph.append(val)
        for j in range(m):
            if val[j] == 0:
                wall_candidates.append((i,j))
            if val[j] == 2:
                viruses.append((i,j))

    res = main(wall_candidates)
    print(res)