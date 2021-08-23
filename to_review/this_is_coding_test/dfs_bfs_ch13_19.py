
def dfs(i, now):
    '''
    모든 경우의 수에 대해, 순차적으로 탐색한다.
    i : 다음인덱스
    now : 지금 인덱스까지 연산한 결과
    '''
    global min_value, max_value, add, sub, mul, div

    #모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if add > 0:
            add -=1
            #다음 인덱스, 지금 인덱스까지 연산한 결과
            dfs(i +1, now + data[i])
            #다음 이터레이션을 위해 원복
            add += 1
        if sub > 0:
            sub -=1
            dfs(i+1, now - data[i])
            sub +=1
        if mul > 0:
            mul -=1
            dfs(i+1, now * data[i])
            mul +=1
        if div > 0:
            div -=1
            dfs(i+1, int(now/data[i]))
            div += 1
    return


if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    # res = solution()
    min_value = 1e9
    max_value = -1e9

    #다음 인덱스, 0번쨰 인덱스까지 연산한 값
    dfs(1, data[0])

    print(min_value)
    print(max_value)