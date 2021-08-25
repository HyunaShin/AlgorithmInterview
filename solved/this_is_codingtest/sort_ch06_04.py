
def solution(k,a,b):
    '''
    a에서 가장 작은 원소를, 배열 B에서 가장 큰 원소와 교체하면 된다.
    이 떄 a 에서 가장 작은 원소가, B에서 가장 큰 원소보다 작을때에만 교체한다.
    '''
    a.sort() #a는 오름차순 정렬
    b.sort(reverse = True) #배열 B는 내림차순 정렬

    for i in range(k):
        #a의 원소가 b의 원소보다 작을 경우
        if a[i] < b[i]:
            #원소를 교체한다
            a[i],b[i] = b[i], a[i]
        else:
            #a의 원소가 b의 원소보다 크거나 같을 때, 반복문을 탈출한다
            # --> b는 내림차순 정렬이므로, 더이상 커질 일이 없음ㅎㅎ
            break
    return sum(a)


def main(k,a,b):
    '''
    반례 : 바꿨는데, b에서 제일 큰원소가 a에서 가장 작은 원소보다 작을 수도 있다.
    '''
    a.sort()
    b.sort()
    for _ in range(k):
        a[:k],b[-k:] = b[-k:], a[:k]

    return sum(a)


if __name__ == "__main__":
    n,k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    ret_main = main()
    ret_solution = solution(k,a,b)

    print(ret_main)
    print(ret_solution)