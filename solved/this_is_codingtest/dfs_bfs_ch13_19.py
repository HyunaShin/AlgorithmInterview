
def dfs(i, now):
    global min_value, max_value, add, minus, mul, div

    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
        return True

    if add > 0:
        add -=1
        dfs(i+1, now + numbers[i])
        add +=1

    if minus > 0:
        minus -=1
        dfs(i + 1, now - numbers[i])
        minus +=1

    if mul > 0:
        mul -= 1
        dfs(i + 1, now * numbers[i])
        mul += 1

    if div > 0:
        div -= 1
        dfs(i + 1, int(now/ numbers[i]))
        div += 1


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split(" ")))
    add, minus, mul, div = list(map(int, input().split()))
    max_value = -1000000001
    min_value = 1000000001
    dfs(1, numbers[0])
    print(max_value)
    print(min_value)