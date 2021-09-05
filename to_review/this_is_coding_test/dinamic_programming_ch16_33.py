import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    t = []
    p = []
    dp = [0] * (n+1)
    for _ in range(n):
        x,y = map(int, sys.stdin.readline().rstrip().split(" "))
        t.append(x)
        p.append(y)

    max_p =0
    for i in range(n-1, -1, -1):
        #오늘 상담 하면 언제 끝나니
        time = t[i] + i
        if time <=n:
            #오늘 상담비 + 다음 상담시 최대 금액
            dp[i] = max(p[i] + dp[time], max_p)
            max_p = dp[i]
        else:
            # 만약 넘어가면, 그날짜 이후로는 돈 못받으니까 max_p유지
            dp[i] = max_p

    print(max_p)

def solution():
    '''
    뒤쪽부터 매 상담에 대해 현재 상담 일자의 이윤 + 상담을 마친 일자부터의 최대 이윤을 계산하면 된다.
    이후 계산된 각각의 값 중에서 최댓값을 출력하면 된다.
    d[i] = i번째 날 부터 마지막 날까지 낼 수 있는 최대 이익
    '''
    n = int(sys.stdin.readline().rstrip())
    t = [] #각 상담을 완료하는데 걸리는 기간
    p = [] #각 상담을 완료했을 때 받을 수 있는 금액
    dp = [0] * (n+1) #다이나믹 프로그래밍을 위한 1차원 dp테이블 초기화
    max_value = 0

    for _ in range(n):
        x,y = map(int, sys.stdin.readline().rstrip().split(" "))
        t.append(x)
        p.append(y)

    #리스트를 뒤에서부터 거꾸로 확인
    for i in range(n-1, -1, -1):
        print(i)
        #상담 끝나는 일자 = 소요일 + 상담일
        time =t[i] +i
        #상담이 기간 안에 끝나는 경우
        if time <= n:
            #지금 이윤, 현재 상담 일자의 이윤 + 상담을 마친 일자부터의 최대 이윤, 최대 이윤
            # print(p[i],[i], dp[time],[time],p[i]+dp[time], max_value)
            dp[i] = max(p[i]+dp[time], max_value)
            max_value = dp[i]
        #상담이 기간을 벗어나는경우
        else:
            dp[i] = max_value

    print(max_value)
    return

if __name__ == "__main__":
    solution()
    main()
