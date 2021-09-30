from itertools import combinations
import copy
n,m,h = map(int, input().split())
# board = [[0] * (n) for _ in range(h-1)]
horizon = []

for _ in range(m):
    a,b = map(int, input().split())
    #b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다
    # board[a-1][b-1] = 1
    horizon.append((b,a-1))

board = []
cases = []
for i in range(h-1):
    board.append([0] * n)
    for j in range(n):
        if (i,j) not in horizon:
            cases.append((i,j))
for x,y in horizon:
    board[x][y] = 1

#세로줄의 좌, 우 정보 만들기
v = dict()
for i in range(n+1):
    v[i+1] = [[-1, i-1], [-1, i]]

def move(v, v_num, board):
    while v[v_num][0][0] < h-2:
        left, right = v[v_num]
        #아래로 가고
        if left[0] < n-1 and right[0] < n-1:
            left[0] +=1
            right[0] +=1
        #왼/오른쪽으로 이동 해야하는 케이스
        #왼쪽으로 이동이 가능하고, 세로줄 왼쪽에 가로줄이 있는 경우
        # print(left[0],left[1])
        if 0 <= left[1] and board[left[0]][left[1]] >= 1:
            #칸 이동
            v[v_num] = [[left[0], left[1]-1], [right[0], right[1]-1]]

        #오른쪽으로 이동이 가능하고, 세로줄 오른쪽에 가로줄이 있는 경우
        elif right[1] < n and board[right[0]][right[1]] >= 1:
            #칸 이동
            v[v_num] = [[left[0], left[1]+1], [right[0], right[1]+1]]

    return v, board

def check_result(v,b):
    # print(v)
    result = 0
    for i in list(v.keys()):#O(N)
        #O(2NH)
        v, b = move(v, i, b)
        if i == v[i][1][1]+1:
            result +=1
    #     print(i, v[i][1][1]+1)
    # print(v)
    # exit()
    if result == h:
        return True
    return False

def main():
    #하나 놔서 되는지
    for i in range(4):
        # print(i)
        if i == 0:
            tb = copy.deepcopy(board)
            tv = copy.deepcopy(v)
            # print(tb)
            # print(tv)
            if check_result(tv, tb):
                return i
        else:
            for case in combinations(cases, i):
                tb = copy.deepcopy(board)
                tv = copy.deepcopy(v)
                for x,y in case:
                    tb[x][y] = 1
                    if check_result(tv, tb):
                        return i
    return -1
result = main()
print(result)
