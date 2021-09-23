from collections import deque

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
# 사과가 있으면 2로 표기
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 2
time_direction = dict()
l = int(input())
for _ in range(l):
    a, b = input().split()
    time_direction[int(a)] = b

def run():
    x, y = 0, 0
    direction = 1
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    q = deque([[x, y]])
    time = 1
    graph[x][y] =1
    while True:
        x, y = x + dx[direction], y + dy[direction]
        if 0 <= x < n and 0 <= y < n and graph[x][y] != 1:
            # 사과가 없다면
            if graph[x][y] != 1:
                tmp_x, tmp_y = q.popleft()
                # 몸 길이를 줄여서 꼬리가 위치한 칸 비우기
                graph[tmp_x][tmp_y] = 0
            # 그럼 머리가 앞으로 가야지
            # 사과가 있으면 머리가 가고, 없으면 꼬리 줄여서 가고
            graph[x][y] = 1
            q.append([x, y])
            # 잎으로 갔으면, 틀지말지 결정
            if time in time_direction.keys():
                if time_direction[time] == "D":
                    direction = (direction + 1) % 4
                else:
                    direction = (direction - 1) % 4
            # 틀기까지 다했으면, 시간 추가
            time += 1
        else:
            return time

print(run())