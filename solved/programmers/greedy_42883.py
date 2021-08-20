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

    while len(number) - 1 > cnt:
        _max = max(number[0: -cnt])
        _max_index = number.index(_max)
        number = number[_max_index + 1:]
        answer += str(_max)
        cnt -= 1

    number = list(map(str, number))
    if cnt < len(number):
        answer += str(max(
            int("".join(number[:-1])), int("".join(number[1:]))))
    else:
        answer += "".join(number)

    return answer

if __name__ == "__main__":
    number = input()
    k = int(input())
    main(number, k)