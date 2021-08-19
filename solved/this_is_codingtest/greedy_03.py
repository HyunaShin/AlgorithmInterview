# -*- coding:utf8 -*-
import sys
import time

def main(rows):
    max_num = -1
    for row in rows:
        min_num = min(row)
        if min_num > max_num:
            max_num = min_num

    return max_num


if __name__ == "__main__":
    n,m = list(map(int, input().split(" ")))
    rows = []
    for i in range(n):
        rows.append(list(map(int, input().split(" "))))
    result= main(rows)
    print(result)