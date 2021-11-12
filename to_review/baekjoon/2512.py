#배정된 에산 중 최댓값 출력하기
#모든 요청이 배정 가능 -> 그대로
#안되면 상한액 계산 -> 그 이상 예산 요청에는 상한액 배정
# 이하는 그대로 배정
#예산 요청은 10만개, 총 예산은 최대 1억
#그러면... 요청은 1~십만까지고, 총 예산은 N에서 1만까지네

# 그럼 상한액은 해봐야 아는거고..
# 그럼 스타트, 엔드는 1~요청의 최댓값 까지
# 찾는 값은 상한액인데 몰라, 상한액을 정하고 배정했을 때 총예산보다만 적으면 돼
def get_total(highst):
    '''요청 금액의 합'''
    res = 0
    for r in requests:
        if r >= highst:
            res += highst
        else:
            res += r
    return res

n = int(input().strip())
requests = list(map(int, input().strip().split()))
m = int(input().strip())
answer = 0
start, end = 0, max(requests)
min_diff = (int(1e9), None)

if sum(requests) >= m:
    #배분해야할 케이스에선
    while start <= end:
        #상한액 : mid
        mid = (start + end)//2
        shared = get_total(mid)
        if shared == m:
            answer = mid
            break
        #배분한 금액이 총 예산보다 크면 -> 배분한 금액 줄이기
        elif shared > m:
            end = mid-1
        #배분한 금액이 총 에산보다 적으면 -> 배분한 금액 늘리기
        elif shared < m:
            diff = m-shared
            #차이가 최소가 되는 예산 얻기
            if min_diff[0] > diff:
                min_diff = (diff, mid)
            start = mid +1

    if answer:
        print(answer)
    else:
        print(min_diff[1])
else:
    print(max(requests))
