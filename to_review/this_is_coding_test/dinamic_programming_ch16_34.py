import sys
def main():
    #가장 긴 증가하는 수열 구하기 문제 유형이다.
    n = int(sys.stdin.readline().rstrip())
    s = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    s.reverse()

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if s[i] > s[j]:
                dp[i] = max(dp[i], dp[j] +1)

    print(n - max(dp))

    return

def solution():
    # '''
    # 가장 긴 증가하는 부분 수열 문제 유형
    # '''
    # n = int(sys.stdin.readline().rstrip())
    # array = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    # #순서를 뒤집어, 가장 긴 증가하는 부분 수열 문제로 변환
    # array.reverse()
    #
    # #다이나믹 프로그래밍을 위한 1차원 DP테이블 초기화
    # dp = [1] * n
    # #가장 긴 증가하는 부분 수열 알고리즘 수행
    # #현재 위치
    # for i in range(1, n):
    #     #현재 위치보다 이전 값
    #     for j in range(0,i):
    #         #현재위치보다 이전값이 작다면, 이전값들을 쭉 둘러보고 dp최댓값 +1을 해 줌
    #         if array[j] < array[i]:
    #             dp[i] = max(dp[i], dp[j] +1)
    #
    # #열외시켜야 하는 병사의 최소 수를 출력
    # print(n-max(dp))

    return

if __name__ == "__main__":
    main()
    # solution()