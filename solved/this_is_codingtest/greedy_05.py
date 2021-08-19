# -*- coding:utf8 -*-

def main(n,m,weights):
    combination = 0
    combination_list = []
    for a in range(n):
        for b in range(n):
            if weights[a] != weights[b]:
                if (a,b) not in combination_list and (b,a) not in combination_list:
                    combination_list.append((a,b))
                    combination += 1

    return combination


def solution(n,m,weights):
    array = [0] * 11

    for x in weights:
        #각 무게에 해당하는 볼링공의 개수
        array[x] += 1

    result =0
    for i in range(1, m+1):
        n -= array[i] #무게가 i인 볼링공의 개수(A가 골랐으니까 줄어들고)
        result += array[i] * n #B가 선택하는 경우의 수 곱하기

    return result

if __name__ == "__main__":
    n,m = list(map(int, input().split(" ")))
    weights = list(map(int, input().split(" ")))
    result = main(n,m,weights)
    print(result)
    sol = solution(n,m,weights)
    print(sol)
