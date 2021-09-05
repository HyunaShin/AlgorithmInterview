import sys

n = int(sys.stdin.readline().rstrip())
k = list(map(int, sys.stdin.readline().rstrip().split(" ")))

dp_tbl = [0] * 100
for i in range(0,n):
    dp_tbl[i] = max(dp_tbl[i-2] + k[i], dp_tbl[i-1])

print(dp_tbl[n-1])