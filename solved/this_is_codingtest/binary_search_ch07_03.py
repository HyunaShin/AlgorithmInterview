import sys

def cut(mid_val, height):
    rice_cake_head = min(mid_val, height)
    rice_cake_tail = height - rice_cake_head
    return rice_cake_tail


def binary_search(start, end, array, mid, target):
    while start <= end:
        height_sum = sum([cut(array[mid],x ) for x in heights])
        if target == height_sum:
            return array[mid]
        elif target < height_sum:
            start = mid +1
            mid = (start + end) //2
        else:
            end = mid -1
            mid = (start + end) //2
    return False


def solution():
    n,m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    array = list(map(int, sys.stdin.readline().rstrip().split()))

    start = 0
    end = max(array)
    result = 0

    while start <= end:
        total = 0
        #절단기 길이 정하기
        mid = start+end //2
        for x in array:
            #잘랐을때의 떡의 양 계산
            if x > mid:
                total += x - mid
        #떡의 양이 부족한 경우 더 자르기(왼쪽 부분 탐색)
        if total < m:
            end = mid -1
        #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
        else:
            #최대한 덜 잘랐을때가 정답이므로, 여기에서 result에 기록
            result = mid
            start = mid +1

    print(result)


    return
if __name__ == "__main__":
    n,m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    heights = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    cutter_candidates = [i+1 for i in range(max(heights))] #O(N)
    mid = len(cutter_candidates)//2

    available_cases = []
    res = binary_search(0,len(cutter_candidates), cutter_candidates, mid, m)
    print(res)
