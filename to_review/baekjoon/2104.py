#i,j에 대해 (a[i] + ... a[j] ) * min(a[i]~a[j])의 최솟값을 곱한 최댓값 구하기
#최댓값을 갖는 부분 배열을 골라내기
#a는 십만개의 1차원 배열
#정수는 백만을 넘지 않음
#그러면 모든 케이스에 대해 부분배열을 골라야하는데, 십만은 순차탐색만 해도.. 200 N으로 풀어야해서 빠듯함
#logN으로 풀자
#A[n]은 랜덤하게 주어진다.
n = int(input().strip())
a = list(map(int, input().strip().split()))
a.sort()
start,end = 0,n
max_val = (0,None)
while start <= end:
    mid = (start + end)//2
    subset = a[start:end]
    subset_val = sum(subset) * min(subset)

    #부분집합이 최댓값 보다 큰 경우
    if subset_val > max_val[0]:
        max_val = (subset_val, start, end)
    #최댓값 보다 작을 때 -> 뒤로 가야될것같은데?
    start = end+1

print(max_val)