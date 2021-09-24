def main():
    n = int(input())
    t, p, visited = [0] * n, [0] * n, [0] * n

    for i in range(n):
        t[i], p[i] = map(int, input().split())


    def dfs(d, c, v):
        global max_cost
        if d + t[d] > n:
            max_cost = max(max_cost, c - p[d])
            return None
        elif d + t[d] == n:
            max_cost = max(max_cost, c)
            return None
        for nd in range(d + t[d], n):
            if v[nd] != 1:
                v[nd] = 1
                dfs(nd, p[nd] + c, v)


    result = 0
    for i in range(n):
        max_cost = 0
        visited[i] = 1
        dfs(i, p[i], visited)
        result = max(result, max_cost)
    print(result)

def solution():
    n = int(input())
    t, p = [], []
    dp = [0] * (n+1)

    for _ in range(n):
        x,y = map(int, input().split())
        t.append(x)
        p.append(y)

    max_p = 0
    #마지막 근무일 부터 백트래킹
    for i in range(n-1, -1, -1):
        #상담이 끝나는 날짜
        time = t[i] + i
        if time <= n:
            #dp 테이블에 최댓값 업데이트
            #지금 최댓값 vs 오늘 상담하면 받을 수 있는 금액 + 상담 끝나면 받을 수 있는 금액
            dp[i] = max(p[i] + dp[time], max_p)
            max_p = dp[i]
        else:
            dp[i] = max_p
    print(max_p)
    return

if __name__ == "__main__":
    # main()
    solution()