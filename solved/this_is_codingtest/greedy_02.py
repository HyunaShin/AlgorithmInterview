# -*- coding:utf8 -*-
import sys
import time

def main(n,m,k, array):
    '''
    array에서 가장 큰 수를 찾아서 K번 더한다.
    M번이 덜 채워 졌다면
    그 다음번 큰 수를 더한다.
    '''
    sorted_arr = sorted(array)
    sorted_arr.reverse()

    multiple = m%k
    moded = m//k

    return (sorted_arr[0] * multiple * k) + (sorted_arr[1] * moded)

if __name__ == "__main__":
    n,m,k = list(map(lambda x : int(x), input().split(" ")))
    array = list(map(lambda x : int(x), input().split(" ")))
    start_tm = time.time()
    print(start_tm)
    result = main(n,m,k,array)
    end_tm = time.time()
    print(end_tm)
    print(end_tm - start_tm)