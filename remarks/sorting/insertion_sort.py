
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    #(움직일 인덱스) 인덱스 i부터 -1까지 감소하며 반복한다
    for j in range(i,0,-1) :
        print(i,j, j-1)
        #움직일 인덱스의 값을 한칸씩 왼쪽으로 이동시킨다.
        if array[i] < array[j-1]:
            #움직일 인덱스가, 왼쪽으로 n칸의 인덱스 보다 작으면 스왑
            array[j], array[j-1] = array[j-1], array[j]
        else:
            #자기보다 작은 데이터를 만나면 그위치에서 멈춤
            break