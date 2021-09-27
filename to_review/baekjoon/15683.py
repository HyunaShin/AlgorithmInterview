from itertools import combinations
import copy
from collections import deque

n,m = map(int, input().split())
cctv_info = {
    1 : [(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1)],
    2 : [(1,0,1,0), (0,1,0,1)],
    3 : [(1,1,0,0), (1,0,0,1), (0,0,1,1), (0,1,1,0)],
    4 : [(1,0,1,1), (0,1,1,1), (1,1,0,1), (1,1,1,0)],
    5 : [(1,1,1,1)]
}
dx, dy = [-1,0,1,0],[0,-1,0,1]
def directing(x,y, d):
    cnt = 0
    dir_path = []
    #감시하는 방향대로
    for i in range(4):
        if d[i] == 1:
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 6:
                dir_path.append((nx, ny))
                nx += dx[i]
                ny += dy[i]
                cnt +=1
    # #감시가 가능한 경로
    return dir_path, cnt


visited= [[ [] for _ in range(m)] for _ in range(n)]
board = [list(map(int, input().split())) for _ in range(n)]
cctv_cnt = 0
to_combine = []
for x in range(n):
    for y in range(m):
        if board[x][y] not in [0,6,"#"]:
            cctv_cnt +=1
            for d in cctv_info[board[x][y]]:
                dir_path, dir_cnt = directing(x, y,d)
                if dir_cnt != 0:
                    # if board[x][y] == 5:
                    #     for i, j in dir_path:
                    #         board[i][j] = "#"
                    # else:
                    to_combine.append((board[x][y], (x, y), dir_path))
# print(to_combine)
# to_combine = []
# print(to_combine, len(to_combine))
result = int(1e9)
for dir_cases in combinations(to_combine, cctv_cnt):
    # print(dir_cases)
    nboard = copy.deepcopy(board)
    dir_list=[]
    for dir_case in dir_cases:
        # print(dir_case)
        if (dir_case[0], dir_case[1]) not in dir_list:
            dir_list.append((dir_case[0], dir_case[1] ))
            for d in dir_case[2]:
                nboard[d[0]][d[1]] = "#"
    cnt = 0
    for i in range(n):
        for j in range(m):
            if nboard[i][j] == 0:
                cnt +=1
    result = min(result, cnt)

print(result)
