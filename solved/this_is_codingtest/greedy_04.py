# -*- coding:utf8 -*-
from itertools import combinations
def main(n, coins):
    coins.sort()
    valid_sum_number = []
    for i in range(n) :
        valid_sum_number += list(map(lambda x : sum(x), combinations(coins,i)))

    valid_sum_number.sort()
    return min(set([i for i in range(0, valid_sum_number[-1])]) - set(valid_sum_number))

if __name__ =="__main__":
    n = int(input())
    coins = list(map(int, input().split(" ")))
    print(main(n, coins))
