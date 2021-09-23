import math
n = int(input())
a = list(map(int, input().split()))
b ,c = map(int,input().split())
result = [0] * n
for i in range(n):
    cnt = 1
    #총감독이 볼 수 있는 수험생 수가, 수햄생 수 보다 크면
    reserved = a[i] - b
    if reserved <= 0:
        result[i]=cnt
    else:
        cnt += math.ceil((a[i]-b)/c)
        result[i] = cnt

print(sum(result))

