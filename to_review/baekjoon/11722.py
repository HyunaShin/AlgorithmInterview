N = int(input())
numbers = list(map(int, input().split()))

#혼자일때 가능한 길이는 1
dp = [1] * N

# numbers돌면서
for i in range(1, N):
    #앞에 숫자랑 비교하기
    for j in range(i):
        #내 앞에 숫자보다 내가 작으면
        if numbers[j] > numbers[i]:
            #내 길이, 내 앞에숫자랑 같이 수열
            dp[i] = max(dp[i], dp[j] +1)

print(max(dp))