import sys

def main():
    #하나씩 추가 해 가면서 해보자
    n = int(sys.stdin.readline().rstrip())
    #배수용 인덱스 초기화
    i2 = i3 = i5 = 0
    next2, next3, next5 = 2,3,5
    dp = [0] * n
    dp[0] = 1
    for l in range(1,n):
        dp[l] = min(next2,next3,next5)
        if dp[l] == next2:
            i2 +=1
            next2 = dp[i2] * 2
        if dp[l] == next3:
            i3 +=1
            next3 = dp[i3] * 3
        if dp[l] == next5:
            i5 +=1
            next5 = dp[i5] * 5

    print(dp[n-1])
    return

def solution():
    n = int(sys.stdin.readline().rstrip())

    ugly = [0] *n #못생긴 수를 담기 위한 테이블(1차원 DP 테이블)
    ugly[0] = 1

    #2배, 3배, 5배를 위한 인덱스
    i2 = i3 = i5 = 0
    #처음에 곱셈 값을 초기화
    #다음으로 와야되는 2의 배수, 3의배수, 5의 배수
    next2, next3, next5 = 2,3,5

    #1부터 n까지의 못생긴 수를 찾기
    for l in range(1,n):
        #가능한 곱셈 결과 중 가장 작은 수를 선택
        #첫번째 : 2
        ugly[l] = min(next2, next3, next5)
        #2가 2의 배수이지?
        if ugly[l] == next2:
            #2배용 인덱스 추가
            i2 +=1
            #다음엔 4를 찾자
            next2 = ugly[i2] * 2
        #그다음엔 3이 왔지?
        if ugly[l] == next3:
            #3배용 인덱스 추가했지?
            i3 +=1
            #다음에는 3의 배수로 6이 와야하지?
            next3 = ugly[i3] * 3
        #4는 위에서 처리했고, 5가 왔지?
        elif ugly[l] == next5:
            #5배용 인덱스 추가
            i5 +=1
            #다음에는 5의 소인수로 25가 와야겠지?
            next5 = ugly[i5] * 5

    print(ugly[n-1])

if __name__ == "__main__":
    main()
    # solution()