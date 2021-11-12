#logN으로 풀어야 하는 문제
#1. 숫자카드를 정렬한다. NlogN -> 50만 * log50만 -> 50만 * 16 -> O(800만)
#2. 정렬한 숫자에서, 찾으려는 숫자보다 크면 왼쪽 작으면 오른쪽으로 고
#3. 숫자와 같으면 결괏값에 추가

n = int(input().strip())
card = list(map(int, input().split()))
m = int(input().strip())
to_find_list = list(map(int, input().split()))

card.sort()
start, end = 0, n
def binary_search(array, start, end, target):
    while start < end:
        mid = (start + end)//2
        if array[mid] == target:
            return array[start:end+1].count(target)
        #찾으려는 값이 미드보다 작다 -> 왼쪽 고
        elif target < array[mid]:
            end = mid-1
        #찾으려는 값이 미드보다 크다 -> 오른쪽 고
        else:
            start = mid +1
    return 0

for to_find in to_find_list:
    res = binary_search(card, 0, n, to_find)
    print(res, end = " ")
