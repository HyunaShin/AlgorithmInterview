# -*- coding:utf8 -*-
import sys
import time
import math

def main(members):
    members.sort()
    sorted_members = list(reversed(sorted(members)))
    num_group = 0
    result = 0 #그룹의 수
    count =0 #그룹에 포함된 모험가 수
    for i in members : # 공포도를 낮은 것 부터 하나씩 확인하며
        count += 1 #현재 그룹에 해당 모험가를 포함시키기
        if count >= i : #현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성
            result += 1
            count =0
    while len(sorted_members):
       max_fear = max(sorted_members)
       num_group +=1
       sorted_members = sorted_members[max_fear:]

    return num_group


if __name__ == "__main__":
    n = list(map(int, input().split(" ")))
    members = list(map(int, input().split(" ")))
    result = main(members)
    print(result)