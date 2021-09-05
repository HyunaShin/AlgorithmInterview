import sys

def main():
    n,m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    array = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index: index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            #왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = max(left_up, left_down, left) + dp[i][j]

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
    return

def solution():
    '''
    왼쪽열 중 어디든 선택해서 시작한다.
    시작점이니 초기화는 원본 값으로 진행한다.
    왼쪽 위, 왼쪽 아래, 왼쪽에서 오는 경우 중 최댓값을 찾는다.
    '''
    n,m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    array = list(map(int,sys.stdin.readline().rstrip().split(" ")))

    dp = []
    index = 0
    #다이나믹 프로그래밍을 위한 2차원 dp테이블 초기화
    for i in range(n):
        dp.append(array[index : index+m])
        index +=m
    #다이나믹 프로그래밍 진행
    for j in range(1,m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            #왼쪽 아래에서 오는경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)

    return

if __name__ == "__main__":
    main()
    # solution()