import sys, math

input = sys.stdin.readline
n = int(input().rstrip())
graph = []
ratio = [0.07, 0.07, 0.02, 0.02, 0.05, 0.1, 0.1, 0.01, 0.01]
dx = [-1, 1, -2, 2, 0, -1, 1, -1, 1]
dy = [0, 0, 0, 0, -2, -1, -1, 1, 1]

start = int(5 / 2) + 1

for _ in range(n):
    graph.append(list(map(int, input().rstrip().split(" "))))
# 현재 포지션 위치
p = (start, start)
# 0 : left, 1 : down, 2: right, 3 : up
state_info = {"u" : (-1,0), "d":(1,0),"l" : (0,-1), "r" :(0,1) }
state = "l"
result = 0
cnt = 1
while p != (1, 1):
    #맨 처음에 현재 위치를 받아온다.
    y, x = p
    #왼쪽으로 이동 해야할 경우
    if state == "l":
        for _ in range(cnt):
            x = x - 1
            # 모래를 이동시킨다.
            remain = graph[x][y]
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    graph[nx][ny] = graph[x][y] * ratio[i]
                    remain -= graph[nx][ny]

        #이동 시켰으면, 다음 칸으로 이동한다.
        p = (x + state_info["d"][0]+1, y + state_info["d"][1])
        state = "d"
    #아래쪽으로 이동 해야할 경우
    elif state == "d":
        for _ in range(cnt):
            y = y + 1
            # 모래를 이동시킨다.
            for i in range(9):
                ny = (x + dx[i]) * -1
                nx = (y + dy[i] ) * -1
                if 0 <= nx < n and 0 <= ny < n:
                    graph[nx][ny] = graph[x][y] * ratio[i]
            #이동 시켰으면, 다음 칸으로 이동한다.
            p = (x + state_info["d"][0], y + state_info["d"][1]+1)
            state = "r"
        cnt +=1

    elif state == "r":
        x = x + 1
        # 모래를 이동시킨다.
        for _ in range(cnt):
            for i in range(9):
                nx = (x + dx[i]) * -1
                ny = (y + dy[i] ) * -1
                if 0 <= nx < n and 0 <= ny < n:
                    graph[nx][ny] = graph[x][y] * ratio[i]

            #이동 시켰으면, 다음 칸으로 이동한다.
            p = (x + state_info["d"][0], y + state_info["d"][1])
            state = "u"
        cnt +=1

    elif state == "u":
        y = y - 1
        # 모래를 이동시킨다.
        for _ in range(cnt):
            for i in range(9):
                ny = (x + dx[i])
                nx = (y + dy[i] )
                if 0 <= nx < n and 0 <= ny < n:
                    graph[nx][ny] += graph[x][y] * ratio[i]

            #이동 시켰으면, 다음 칸으로 이동한다.
            p = (x + state_info["d"][0], y + state_info["d"][1])

