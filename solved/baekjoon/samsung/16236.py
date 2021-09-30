from collections import deque
n=int(input())
board=  [list(map(int, input().split())) for _ in range(n)]
fishes = []
shark = None
dx,dy = [-1,0,1,0], [0,-1,0,1]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            #상어 x,y, 경과한 시간, 크기, 물고기 먹은 횟수
            shark=[i,j,0,2,0]
        elif 1<= board[i][j]<=6:
            #물고기 x,y, 거리
            fishes.append([i,j,int(1e9)])

def bfs(x,y, target_x, target_y, cnt, size):
    #맨처음 아기상어 위치
    q = deque()
    visited=set()
    visited.add((x,y))
    q.append((x,y, target_x, target_y, cnt, size))

    while q:
        x,y, target_x, target_y, cnt, size = q.popleft()
        if (x,y) == (target_x, target_y):
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 상어보다 크기가 크면 못지나간다는 조건
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] <= size and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.append((nx, ny, target_x, target_y, cnt +1, size))
    #못가는 경우(큰물고기가 있어서)
    return int(1e9)

while True:
    sx, sy, time, size, trial = shark
    if size == trial:
        size +=1
        trial = 0

    for i in range(len(fishes)):
        fx, fy, distance = fishes[i]
        #나보다 물고기의 크기가 작다면
        if board[fx][fy] < size:
            #물고기의 거리 구하기, 확인필
            distance = bfs(sx, sy, fx, fy, 0, size)
            #물고기의 최소 거리 업데이트
            fishes[i][2] = distance
    #이제 최소거리 구했으니까, 정렬(거리 가까운순, 가장 위에있는, 가장 왼쪽에 있는)
    if len(fishes):
        fishes.sort(key=lambda x : (x[2],x[0],x[1]))
        nx, ny, distance = fishes.pop(0)
        #정렬 했을 때, 먹을만한게 없다면, 멈춤
        if distance == int(1e9) or board[nx][ny] >= size:
            continue
        #물고기가 상어보다 작다면, 이동과 동시에 물고기를 먹는다
        if board[nx][ny] < size:
            board[nx][ny] = 9
            board[sx][sy] = 0
            #자신의 크기와 같은 수의 물고기가 아니니, 크기는 그대로, 시도횟수 증가
            shark = (nx, ny, time+distance, size, trial+1)
    else:
        break

print(shark[2])

