import sys
input = sys.stdin.readline
n,m = map(int, input().strip().split())
board = [[0]*(m+1)] + [[0] + list(map(int, input().strip().split())) for _ in range(n)]
dp_tbl = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp_tbl[i][j] = board[i][j] + max(dp_tbl[i-1][j-1], dp_tbl[i-1][j], dp_tbl[i][j-1])
print(dp_tbl[n][m])