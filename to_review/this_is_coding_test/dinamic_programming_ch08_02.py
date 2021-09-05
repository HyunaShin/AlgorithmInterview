import sys

dp_tbl = [0] * 30001
def main(x):
    for i in range(2, x+1):
        #바텀업에서 한칸 올라갈 때 마다 연산 한번
        dp_tbl[i] = dp_tbl[i-1] +1
        if i%2 == 0:
            # 이전보다 한번 더 연산하기 vs 2로 나눈 케이스의 노드에서 한 연산 횟수 +1
            dp_tbl[i] = min(dp_tbl[i], dp_tbl[i//2] +1)
        if i%3 == 0:
            # 이전보다 한번 더 연산하기 vs 3로 나눈 케이스의 노드에서 한 연산 횟수 +1
            dp_tbl[i] = min(dp_tbl[i], dp_tbl[i//3] +1)
            # 이전보다 한번 더 연산하기 vs 3로 나눈 케이스의 노드에서 한 연산 횟수 +1
        if i%5 == 0:
            dp_tbl[i] = min(dp_tbl[i], dp_tbl[i//5] +1)
    return dp_tbl[x]



def solution():
    x = int(sys.stdin.readline().rstrip())
    d = [0] * 30001
    for i in range(2, x +1):
        d[i] = d[i-1] +1
        if i%2 ==0:
            d[i] = min(d[i], d[i//2] +1)
        if i%3==0:
            d[i] = min(d[i], d[i//3] +1)
        if i%5 == 0:
            d[i] = min(d[i], d[i//5] +1)
    return

if __name__ == "__main__":
    x = int(sys.stdin.readline().rstrip())
    res = main(x)
    print(res)