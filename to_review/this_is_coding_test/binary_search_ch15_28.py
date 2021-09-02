import sys

def main(start, end):
    while start <= end:
        mid = (start + end) // 2
        print(start, end, mid)
        if mid == array[mid]:
            return mid
        elif array[mid] < mid :
            start = mid+1
        else:
            end = mid - 1

def solution( array, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return solution(array, start, mid-1)
    else:
        return solution(array, mid+1, end)

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    ret = main(0,n)
    # print(ret)
    # ret = solution(array,0, n)
    if ret != None:
        print(ret)
    else:
        print(-1)