
def sequential_search(n, target, array):
    #각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재 원소가 찾고자 하는 원소와 동일한 경우
        if array[i]== target:
            return i+1 #현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)

if __name__ == "__main__":
    print("생성할 원소 갯수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
    input_data = input().split()
    n = int(input_data[0]) #원소의 갯수
    target = input_data[1] #찾고자하는 문자열

    print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄워쓰기 한칸으로 합니다.")
    array = input().split()

    print(sequential_search(n, target, array))