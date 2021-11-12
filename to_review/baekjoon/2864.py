import sys
input = sys.stdin.readline
a,b = input().strip().split()

min_val, max_val = int(1e9), 0

case1 = int(a) + int(b)
min_val = min(min_val, case1)
max_val = max(max_val, case1)

case2 = int(a.replace("5", "6")) + int(b.replace("5", "6"))
min_val = min(min_val, case2)
max_val = max(max_val, case2)

case3 = int(a.replace("6", "5")) + int(b.replace("6", "5"))
min_val = min(min_val, case3)
max_val = max(max_val, case3)

print(min_val, max_val)