def main(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_cnt_plus = [i for i in range(len(alphabet))]
    alphabet_cnt_minus = [i - len(alphabet) for i in range(len(alphabet))]

    movements = 0
    for i in name:
        if i != "A":
            to_right = alphabet.find(i)
            if abs(alphabet_cnt_plus[to_right]) < abs(alphabet_cnt_minus[to_right]):
                # 위로 이동
                movements += to_right
            else:
                # 아래로 이동
                movements += abs(alphabet_cnt_minus[to_right])
        else:
            # 오른쪽으로 이동
            movements += 1
    return movements

def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        #위로 몇번/아래로 몇번 이동해야하는지에 대한 리스트
        num_char = [i for i in range(14)] + [j for j in range(12,0,-1)]
        #현재 알파벳의 인덱스가 A로부터 얼마나 떨어져있는지
        return num_char[ord(char) - ord('A')]

    #위/아래로 몇번 이동해야되는지
    for ch in name:
        answer += alphabet_to_num(ch)

    move = n-1
    for idx in range(n):
        #name에서 한칸씩 검사
        next_idx = idx +1
        #다음 인덱스의 알파벳이 A고, 마지막 인덱스가 아니라면(A가 여러개인 케이스)
        while (next_idx < n) and (name[next_idx] == 'A'):
            #다음 인덱스로 이동
            next_idx +=1

        #지금 인덱스 vs A가 아닌 인덱스를 뒤에서 접근
        distance = min(idx, n - next_idx)
        #
        move = min(move, idx + n - next_idx + distance)


if __name__ == "__main__":
    name = input()
    ret = main(name)
    print(ret)