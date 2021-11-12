import sys
sys.setrecursionlimit(2000)
n = int(sys.stdin.readline().rstrip())
d = [0] * (n+1)

for i in range(2, n+1):
    #연산 횟수는 이전 연산횟수+1
    #인덱스 : 해당 수가 되는 최소 연산 횟수
    #i가되려면 i-1 에서 1을 더해줘야겠지?
    d[i] = d[i-1] +1
    #i가 3으로 나눠떨어지려면, i//3번째에서 *3을 해주거나, 이전 연산 중 젤 최솟값이겠지?
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    #2로 나누어 떨어질 때, i//2해줬을 때 *2를 해줬거나 더 최솟값이 있겠지?
    if i %2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[n])