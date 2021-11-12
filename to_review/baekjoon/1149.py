import sys
input = sys.stdin.readline
n = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(n)]
for i in range(1,n):
    board[i][0] = min(board[i-1][1], board[i-1][2]) + board[i][0]
    board[i][1] = min(board[i - 1][2], board[i - 1][0]) + board[i][1]
    board[i][2] = min(board[i - 1][1], board[i - 1][0]) + board[i][2]
print(min(board[-1]))