import sys
def main(start ,end, mid, target, array):
    visited = []
    cnt = 0
    start_info = False
    end_info = False
    while start <= end:
        print(start ,end, mid, target)
        if array[mid] == target:
            cnt +=1
            if start_info:
                visited.append(mid)
                start = max(mid-1, 0)
            elif end_info:
                end = min(mid+1, end)
            # end = min(,end)
            # start = mid

        elif target> array[mid]:
            start = mid +1
            start_info = True
            end_info = False
        else:
            end = mid -1
            start_info = False
            end_info = True
    return visited

if __name__ == "__main__":
    n,m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    mid = (0+n)//2

    res = main(0,n-1, mid, m, arr)
    print(res)