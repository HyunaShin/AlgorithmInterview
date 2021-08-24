# -*- coding:utf8 -*-
from itertools import combinations

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)
    return

def count_safe_zone():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt +=1
    return cnt

def main():
    global tmp
    max_cnt = -1
    for walls in combinations(wall_candidates, 3):
        #원래 벽
        for i in range(n):
            for j in range(m):
                    tmp[i][j] = graph[i][j]
        #벽 세개 새우기
        for x,y in walls:
            tmp[x][y] = 1

        for x,y in virus_loc:
            virus(x,y)
        max_cnt = max(max_cnt, count_safe_zone())

    return max_cnt


if __name__ == "__main__":
    n,m = map(int, input().split(" "))
    graph = []
    tmp = []
    virus_loc = []
    wall_candidates = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        graph.append(list(map(int, input().split(" "))))
        tmp.append([0] * m)
        for j in range(m):
            if graph[i][j]  == 0:
                wall_candidates.append((i,j))
            if graph[i][j] == 2:
                virus_loc.append((i,j))

    res = main()
    print(res)