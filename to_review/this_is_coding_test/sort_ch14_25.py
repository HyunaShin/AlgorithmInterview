def main(N, stages):
    stooked_info = [0] * (N + 2)
    fail_rate = [0] * (N + 2)
    for i in range(N + 2):
        for stook in stages:
            if i == stook:
                stooked_info[i] += 1

    for i in range(N + 2):
        if i > 0:
            staged = sum([x[1] for x in enumerate(stooked_info[i: N + 2])])
            if staged:
                fail_rate[i] = (i, stooked_info[i] / staged)
            else:
                fail_rate[i] = (i, 0)
    ans = fail_rate[1:-1]
    ans.sort(key=lambda x: (-x[1], x[0]))
    return list(map(lambda x: x[0], ans))


def solution(N, stages):
    answer = []
    #사람 몇명있는지
    length = len(stages)
    #스테이지 번호를 1부터 N까지 증가시키며
    for i in range(N+1):
        #해당 스테이지에 머물러있는 사람 수 계산
        count = stages.count(i)

        #실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count/length

        answer.append((i,fail))
        length -= count

    answer = sorted(answer, key=lambda t : t[1], reverse = True)
    answer = [i[0] for i in answer]
    return answer