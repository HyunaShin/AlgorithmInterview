import sys

def main(start, end, c):
    #탐색 대상 : 가장 접한 두 공유기 사이의 거리
    #가장 먼저 Base Case로 첫번째 집에 공유기를 설치한다(사이즈가 안나오면, 탐색 하면서 찾게 되있따)
    array.sort()
    value = array[0]
    #공유기 거리의 범위는 다음과 같다.
    start = 1
    end = array[-1]
    while start <= end:
        cnt = 1 #첫번째 집에 설치 됐으므로
        mid = (start + end) // 2
        for i in range(1,end):
            if array[i] >= value + mid:
                value = array[i]
                cnt += 1

        if cnt >= c:
            #인접한 두 집 사이의 거리를 늘린순 없는지 체크
            start = mid +1
            result = mid
        else:
            end = mid-1

    print(result)

    return

def solution():

    n,c = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    array = []
    for _ in range(n):
        array.append(int(input()))
    #이진 탐색을 위해 정렬 수행
    array.sort()
    #gap의 최소, 최대가 될 수 있는 값
    start = 1 #최소 1
    end = array[-1] - array[0] #가능한 최대 거리
    result = 0

    while(start <= end):
        #mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미함.
        mid = (start + end) // 2

        #최대거리, 일단 첫번쨰 집에 설치
        value = array[0]
        #일단 첫번째 집에 설치
        count = 1
        #현재의 mid값을 이용해 공유기를 설치
        for i in range(1,n):
            # 앞에서부터 차근차근 설치한다.
            # gap(찍은 값)이 아니라, 실제 두 공유기 사이의 거리를 취하기 위함
            if array[i] >= value + mid:
                # 최대 거리를 갱신
                value = array[i]
                count +=1

        #c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        if count >= c:
            start = mid +1
            result = mid
            #최적의 결과를 저장
        else:
            #C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
            end = mid-1
    print(result)
    

    return

if __name__ == "__main__":
    n,c = list(map(int, sys.stdin.readline().split(" ")))
    x_list = [int(sys.stdin.readline()) for _ in range(n)]
    #O(NlogN)
    x_list.sort()
    array = [i for i in range(x_list[-1])]
    # wifi = []
    main(0, x_list[-1], c)
    # print(wifi)
    # solution()