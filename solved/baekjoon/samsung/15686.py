from itertools import combinations

n,m = map(int, input().split())
board = []
stores = {}
houses = dict()
idx = 0
for i in range(n):
    board.append(list(map(int, input().split())))
    #m개의 치킨집에 대한 정보를 담고 있는, (i,j) 위치의 집
    for j in range(n):
        if board[i][j] == 1:
            houses[(i,j)]=[]
        elif board[i][j] == 2:
            stores[(i,j)] =idx
            idx +=1


#1. 집별로 치킨집과의 거리 구하기
for h in list(houses.keys()):
    hx, hy = h
    #치킨집의 좌표
    for c,c_idx in stores.items():
        houses[h].append( (abs(hx - c[0]) + abs(hy - c[1])))

result = int(1e9)
for cases in combinations(list(stores.values()),m):
    city_distance = 0
    #집과 치킨집과의 거리를 가져와서
    for h in houses.keys():
        chicken_distance = int(1e9)
        #지금 고른 경우의 수에서 치킨 거리를 구해보자
        for c in cases:
            chicken_distance = min(houses[h][c], chicken_distance)
        city_distance += chicken_distance
    result = min(result, city_distance)
print(result)
