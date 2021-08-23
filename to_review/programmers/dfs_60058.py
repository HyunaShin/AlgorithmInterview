from collections import deque


def dfs(idx, visited, p):
    stack = deque()
    stack.append(idx)
    visited[idx] = True

    while stack:
        print(visited, stack)
        if idx >= len(p) - 1:
            break

        if visited[idx + 1] != stack[0]:
            idx += 1
            visited[idx] = True
            stack.pop()
        else:
            idx += 1
            visited[idx] = True
            stack.append(idx)

    return visited


def balanced_index(p):
    '''균형잡힌 괄호 문자열의 인덱스 반환'''
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count +=1
        else:
            count -=1
        if count == 0:
            return i
    return

def check_proper(p):
    count = 0
    for i in p:
        if i == "(":
            count +=1
        else:
            #쌍이 안맞으면 False
            #룹 다 돌기 전에 count가 0이 되면, 짝이 안맞다는 소리
            if count == 0:
                return False
            count -=1
    return True #쌍이 맞으면 True


def solution(p):
    answer = ''
    if p == '':
        return answer

    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]

    if check_proper(u):
        answer = u + solution(v)

    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)

    return answer


if __name__ == "__main__":
    p = input()
    start = 0
    visited = [False] * len(p)

    dfs(start, visited, p)