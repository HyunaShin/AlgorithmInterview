import sys
n,m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
price = dict()
for i in range(n):
    price[i] = int(sys.stdin.readline().rstrip())


d = [0] * 100001
for money in range(m):
    max_price = 0
    #사용 가능한 최대 화폐 찾기
    #최대 화폐보다 적은 원일 경우엔
    if price[n] > money:
        for i in range(n-1):
            #화폐 사이에 끼거나
            if price[i-1] < money < price[i+1]:
                max_price = price[i-1]
            #화폐와 같거나
            elif price[i] == money:
                max_price = price[i]
            #최소 화폐보다도 적다.
            else:
                pass
    #쓸 수 있는 화폐가 없으면, 못만든다.
    if max_price != 0:
        d[money] = -1
    #쓸 수 있는 화폐가 있다면
    else:
        #최대 화폐 금액을 돌면서 화폐를 만들 수 있는 최소 횟수를 찾는다.
        #1원만 모조리 더해도, 나올 수 없는 값을 넣어준다.
        min_cnt = 10002
        for p in range(max_price):
            min_cnt = min(min_cnt, d[money - p] + p)
        d[money] = min_cnt
print(d[m-1])












