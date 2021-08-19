# -*- coding:utf8 -*-
import sys
import time
import math

def main(n,k):
    to_multiply = 0
    for i in range(0,100000):
        if (k ** i <= n) & (k ** (i+1) > n):
            to_multiply = i
            break
    to_minus = n-(k ** to_multiply)
    return to_minus + to_multiply


if __name__ == "__main__":
    n, k = list(map(int, input().split(" ")))
    result = main(n,k)
    print(result)