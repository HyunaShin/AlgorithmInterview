# -*- coding:utf8 -*-

def main(number, k):
    '''
    cnt : number -k(남은 숫자 수)
    - [0: -cnt 번째 인덱스]의 수까지 찾아보기
    - 선정한 첫번째 자리수를 string에 추가
    - 숫자에서 선정한 첫번째 자릿수까지 삭제
    - 선정한 숫자를 string에 추가
    - 선정한 숫자의 자리수 까지 삭제
    '''
    answer = ''
    number = list(map(int, number))
    cnt = len(number) - k
    #100만번 룹을 돌면서
    while len(number) - 1 > cnt:
        #최댓값 찾는 연산 하면서
        _max = max(number[0: -cnt])
        #인덱스 찾는 연산
        _max_index = number.index(_max)
        number = number[_max_index + 1:]
        answer += str(_max)
        cnt -= 1
    else:
        answer += str(max(int("".join(list(map(str, number[:cnt])))), int("".join(list(map(str, number[-cnt:]))))))

    return answer

def solution(number, k):
    '''
    스택은 무조건 전 인덱스 보다 큰 숫자만 들어간다.
    k개 뺀 인덱스 까지를 리턴
    k = 4, 지금 4
    4177252841 ->  [4]
    k = 4, 지금 1
    4177252841 ->  [4,1]
    k=4, 지금7
    1) 1<7 k = 4 --> k =3, [4]
    2) 4<7 k = 3 --> k = 2 []
    --> [7]
    # 4177252841 ->  []

    252841 -> max(25) => 5
    cnt = 3
    2841 ->
    40분 걸림ㅠㅠ

    '''
    answer = ''
    stk = []
    for i in number:
        while stk and stk[-1] < i and k>0:
            # 제일 큰 숫자만 남게끔 도로 지우기
            k-=1
            stk.pop()
        stk.append(i)
    return "".join(stk[:len(stk)-k])

if __name__ == "__main__":
    number = input()
    k = int(input())
    main(number, k)