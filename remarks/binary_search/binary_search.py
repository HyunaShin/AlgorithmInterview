def binary_search_loop(array, target, start, end):
    while start <= end :
        mid = (start + end)//2

        if array[mid] == target:
            return mid
        #중간점의 값 보다 찾고자 하는 값이 작은 경우
        elif array[mid] > target:
              end = mid-1
        #중간점의 값보다 찾고자 하는 값이 작은 경우
        else:
            start = mid+1
    return None




def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
    # 중간점의 값보다 작다는건 아는거니까, 중간점 앞의 인덱스로 종점 이동
    elif array[mid] >target:
        return binary_search_recursive(array,target, start ,mid-1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search_recursive(array, target, mid+1, end)


if __name__ == "__main__":
    #n(원소의 개수) 와 target(찾고자 하는 문자열)을 입력 받기
    n, target = list(map(int, input().split(" ")))
    #전체 언소 입력 받기
    array = list(map(int, input().split()))

    # result = binary_search_recursive(array, target, 0, n-1)

    result = binary_search_recursive(array, target, 0, n-1)
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result +1)