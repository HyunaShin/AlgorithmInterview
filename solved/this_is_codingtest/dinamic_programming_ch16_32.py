import sys

def solution():
    '''
    탑다운으로 가되, 벗어나는 범위만 잘 체크하는 로직으로 구성함
    '''
    n = int(sys.stdin.readline().rstrip())
    dp = []
    for _ in range(n):
        dp.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

    for i in range(1,n):
        for j in range(i+1):
            #왼쪽 위에서 내려오는 경우
            if j == 0:
                up_left = 0
            else:
                up_left = dp[i-1][j-1]
            #바로 위에서 내려오는 경우
            if j == i:
                up = 0
            else:
                up = dp[i-1][j]

            dp[i][j] = dp[i][j] + max(up,up_left)
    print(max(dp[n-1]))


    return

def main():
    # n = int(sys.stdin.readline().rstrip())
    # t = []
    # for _ in range(n):
    #     t.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    #
    # #dp테이블은 그대로 쓴다.
    # for i in reversed(range(0,n-1)):
    #     for j in range(i+1):
    #         t[i][j] = t[i][j] + max(t[i+1][j], t[i+1][j+1])
    #
    # print(t[0][0])
    return

if __name__ == "__main__":
    # main()
    solution()