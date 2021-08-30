import sys


def main():
    n, x = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    array = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    #시작 인덱스 찾고
    def get_start_idx(start, end, target):
        if start > end:
            return None
        mid = (start + end)// 2
        if (mid == 0 or target > array[mid -1]) and array[mid] == target:
            return mid
        #같은 수가 여러번 나오므로
        elif target <= array[mid] :
            return get_start_idx(start, mid-1, target)
        else:
            return get_start_idx(mid+1, end, target)

    #끝 인덱스 찾고
    def get_end_idx(start, end, target):
        if start > end:
            return None
        mid = (start + end)// 2
        if (mid == n-1 or target < array[mid +1]) and array[mid] == target:
            return mid
        elif  target < array[mid]:
            # return get_end_idx(start, mid-1, target)
            return get_end_idx(start, mid-1, target)
        else:
            return get_end_idx(mid+1, end, target)
    # 끝 - 시작 +1 을 해 주기

    start_idx = get_start_idx(0, n, x)
    end_idx = get_end_idx(0,n,x)
    if start_idx != None and end_idx != None:
        return (end_idx - start_idx) +1
    else:
        return -1


def count_by_value(array, x):
    #데이터의 갯수
    n = len(array)
    #x가 처음 등장한 인덱스 계산
    a = first(array,x, 0, n-1 )
    if a == None:
        #값이 x인 원소의 개수는 0개이므로 0 반환
        return 0
    b = last(array, x, 0, n-1)
    return b - a +1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    #해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    #왜 이 조건문 한줄로 모든 처리가 다 되는거지?
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid -1)
    else:
        #조건 만족 안하면, 시작 지점 땡겨옴
        return first(array, target, mid +1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    #해당 값을 갖고 있는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    #중간점의 값 보다 찾고자하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid -1)
    #중간점의 값보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return last(array, target, mid+1, end)


if __name__ == "__main__":
    # 1. 정렬 된 수열로 들어온다.
    # 2. 따라서 이진 탐색이 가능하고
    # 3. 찾으려는 수의 시작 인덱스, 종료 인덱스를 찾으면 된다.
    n,x = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    array = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    count = count_by_value(array, x)
    if count == 0:
        print(-1)
    else:
        print(count)
    # ret = main()
    # print(ret)