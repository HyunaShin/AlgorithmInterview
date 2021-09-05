import sys

n = int(sys.stdin.readline().rstrip())
t = []
for _ in range(n):
    t.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

#dp테이블은 그대로 쓴다.
for i in reversed(range(0,n-1)):
    for j in range(i+1):
        t[i][j] = t[i][j] + max(t[i+1][j], t[i+1][j+1])

print(t[0][0])