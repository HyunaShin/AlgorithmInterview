from collections import deque


def mk_union(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    unions[x][y] = index
    summary = geoinfo[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n  and unions[nx][ny] == -1:
                if l <= abs(geoinfo[nx][ny] - geoinfo[x][y]) <= r:
                    q.append((nx, ny))
                    #연합 추가됨 표기
                    unions[nx][ny] = index
                    summary += geoinfo[nx][ny]
                    count +=1
                    united.append((nx, ny))
    for i,j in united:
        geoinfo[i][j] = summary//count

if __name__ == "__main__":
    n, l, r = list(map(int, input().split(" ")))
    geoinfo = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        geoinfo.append(list(map(int, input().split(" "))))

    #여기에 왜 while문이 들어가는지 모르겠고
    # --> 그래프는 계속 업데이트 되니까, 총 몇번 연합을 열고/닫았는지가 키포인트
    total_count = 0
    while True:
        # 연합에 안 들어간 나라가 있으면, 그 나라 기준으로 돌게 해야함.
        # 이 때, 연합을 한번 맺은 상태라면 더이상 이동을 못하니 다음번째 연합으로 넘어감
        unions = [[-1] * n for _ in range(n)]
        index = 0
        for i in range(n):
            for j in range(n):
                # 연합에 안들어있으면
                if unions[i][j] == -1:
                    # 탐색 시작
                    mk_union(i, j, index)
                    index += 1
        if index == n*n:
            break
        total_count += 1

    print(total_count)

    # move_cnt = 0
    # united = bfs(0,0)
    # while len(united):
    #     geo_num = 0
    #     for nation in united:
    #         geo_num += geoinfo[nation[0]][nation[1]]
    #
    #     updated_geo = int(geo_num/len(united))
    #     for nation in united:
    #         geoinfo[nation[0]][nation[1]] = updated_geo
    #         move_cnt +=1
    #     united = bfs(0,0)

# ========origin==========
#
# def bfs(x,y):
#     q = deque()
#     q.append((x,y))
#
#     united = []
#     while q:
#         print(q)
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx >= 0 and nx < n and ny >= 0 and ny < n:
#                 geo_diff = abs(geoinfo[x][y] - geoinfo[nx][ny])
#                 if geo_diff >= l and geo_diff <= r and (nx,ny) not in united:
#                     united.append((nx,ny))
#                     q.append((nx,ny))
#     return united
#
#
# if __name__ == "__main__":
#     n, l, r = list(map(int, input().split(" ")))
#     geoinfo = []
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     for i in range(n):
#         geoinfo.append(list(map(int, input().split(" "))))
#
#     move_cnt = 0
#     united = bfs(0,0)
#     while len(united):
#         geo_num = 0
#         for nation in united:
#             geo_num += geoinfo[nation[0]][nation[1]]
#
#         updated_geo = int(geo_num/len(united))
#         for nation in united:
#             geoinfo[nation[0]][nation[1]] = updated_geo
#             move_cnt +=1
#         united = bfs(0,0)
