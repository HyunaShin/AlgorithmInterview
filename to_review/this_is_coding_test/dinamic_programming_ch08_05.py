import sys

def solution():
    n,m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    array = []
    for _ in range(n):
        array.append(int(sys.stdin.readline().rstrip()))
    d = [10001] * m+1

    d[0] = 0
    for i in range(n):
        #array의 값은,
        for j in range(array[i], m+1):
            #(i-k)원을 만드는 방법이 존재 하는 경우
            if d[j - array[i]] != 10001:
                d[j] = min(d[j], d[j - array[i]] +1)
    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])
    return

def main():
    n,m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    price_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    d = [10001] * (m+1)
    d[0] = 0
    #화폐 단위로 룹 돌림
    for price in price_list:
        #화폐 단위~목표 금액까지 룹을 돌리면서, 최소 횟수를 업데이트 시킴
        for i in range(price,m):
            if d[i-price] != 10001:
                d[i] = min(d[i], d[i-price]+1)

    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])

    # for i in range(n):
    #     price[i] = int(sys.stdin.readline().rstrip())
    #
    # d = [0] * 100001
    # for money in range(m):
    #     max_price = 0
    #     #사용 가능한 최대 화폐 찾기
    #     #최대 화폐보다 적은 원일 경우엔
    #     if price[n-1] >= money:
    #         for i in range(1, n-1):
    #             print(money, price[n - 1])
    #             #화폐 사이에 끼거나
    #             if max(price[i-1], 0) < money < price[i+1]:
    #                 max_price = price[i-1]
    #                 print("price < money < price : %d, price : %d, %d"%(money,price[i-1],price[i+1]))
    #             #화폐와 같거나
    #             elif price[i] == money:
    #                 # print(i)
    #                 max_price = price[i]
    #                 # d[i] = price[i]
    #                 print("price == money : %d, price : %d"%(price[i],money))
    #             #최소 화폐보다도 적다.
    #             else:
    #                 print("lower then comparison money : %d, price : %d"%(money, price[n-1]))
    #         #쓸 수 있는 화폐가 없으면, 못만든다.
    #         if max_price == 0:
    #             d[money] = -1
    #         else:
    #             min_cnt = 10002
    #             for p in range(max_price):
    #                 min_cnt = min(min_cnt, d[money - p] + 1)
    #             d[money] = min_cnt
    #
    #     #쓸 수 있는 화폐가 있다면
    #     else:
    #         #최대 화폐 금액을 돌면서 화폐를 만들 수 있는 최소 횟수를 찾는다.
    #         #1원만 모조리 더해도, 나올 수 없는 값을 넣어준다.
    #         min_cnt = 10002
    #         for p in range(max_price):
    #             min_cnt = min(min_cnt, d[money - p] + p)
    #         d[money] = min_cnt
    # print(d[:m])



if __name__ == "__main__":
    main()


