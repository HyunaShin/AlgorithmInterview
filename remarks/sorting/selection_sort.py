array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    #가장 작은 원소의 인덱스
    min_index = i
    # 정렬 안된 인덱스 중에서 가장 작은 값의 인덱스를 찾는다.
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    #가장 작은 값의 인덱스를 찾으면 스왑
    # 스왑 : 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업
    array[i], array[min_index] = array[min_index], array[i]
print(array)