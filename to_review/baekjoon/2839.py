n = int(input())
d = [int(1e9)] * (n+1)
for i in range(3,n+1):
    #이전의 최솟값 +3kg or +5kg?
    d[i] = min(d[i-3]+1, d[i-5]+1)
    #이전의 최솟값 +3kg or +5kg? 아님 3키로만?
    if i%3 == 0:
        d[i] = min(d[i-3]+1,d[i-5]+1,i//3)
    if i%5 == 0:
        # 이전의 최솟값 +3kg or +5kg? 아님 5키로만?
        d[i] = min(d[i-3]+1, d[i - 5]+1, i//5)

if d[n] >= int(1e9):
    print(-1)
else:
    print(d[n])
