# -*- coding:utf8 -*-

def main(s):
    result = s[0]
    for i in s[1:]:
        if i <= 1 or result <= 1: #둘중 하나가 1보다 작으면, 더하는게 더 큰 수임
            result += i
        else:
            result *= i
    return result

if __name__ == "__main__":
    s = list(map(int, input()))
    result = main(s)
    print(result)

