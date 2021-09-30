from collections import deque
n, l, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx= [0,1,0,-1]
dy = [-1,0,1,0]

def union(a,b):
    q = deque()
    q.append((a,b))
    union_list = [(a,b)]
    while q:
        #한 나라를 찍고
        x,y= q.popleft()
        # union_list.append()
        #상하좌우(국경을 공유하는 다른 나라)
        for i in range(4):
            nx,ny = dx[i]+x, dy[i] + y
            if 0<= nx < n and 0 <= ny <n:
                diff = abs(board[x][y] - board[nx][ny])
                #인구 차이가 l명이상 r명 이하라면 국경을 연다
                if  l <= diff <= r and (nx,ny) not in union_list:
                    q.append((nx, ny))
                    union_list.append((nx,ny))
                    # print(nx, ny , x, y, q, union_list)
                # else:
                #     union_list.remove((nx,ny))
                    # union_list.pop(-1)
    return union_list
# print(board)
day = 0
while True:
    trial = 0
    union_cases = []
    for i in range(n):
        for j in range(n):
            union_list = union(i,j)
            people = 0
            for u in union_list:
                people += board[u[0]][u[1]]
            dp = int(people/len(union_list))
            for u in union_list:
                board[u[0]][u[1]] = dp

            if len(union_list) != 1:
                trial+=1
                if set(union_list) not in union_cases:
                    union_cases.append(set(union_list))
                    day += 1
            print(union_list,set(union_list) , day)
    if trial == 0:
        break

print(board)
print(day)
print(union_cases)
