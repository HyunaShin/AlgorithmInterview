def solution(N, stages):
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

