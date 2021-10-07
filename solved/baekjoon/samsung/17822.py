from pprint import pprint
n,m,t = map(int, input().split())
board = [[0] * m]
for _ in range(n):
    board.append(list(map(int, input().split())))

#  번호가xi인 원판을, di방향으로, ki칸 회전
t_list = [list(map(int, input().split())) for _ in range(t)]

def turn(x, d, k):
    tmp_n = list(filter(lambda y : y%x==0,range(1,n+1)))
    if d == 0: #시계방향
        for i in tmp_n:
            tmp = [0] * m
            for j in range(m):
                tmp[(j+k)%m] = board[i][j]
            #다 돌렸으면 원판에 할당
            board[i] = tmp
    else:
        for i in tmp_n:
            tmp = [0] * m
            for j in range(m):
                # print()
                tmp[j-k] = board[i][j]
            #다 돌렸으면 원판에 할당
            board[i] = tmp
    return

def check(i,j):
    val = board[i][j]
    to_flag = []
    if i == 1:
        if val == board[2][j] and val != int(1e9):
            to_flag.append((2,j))
    elif i == n:
        if val == board[n-1][j] and val != int(1e9):
            to_flag.append((n-1,j))
    else:
        if val == board[i-1][j] and val != int(1e9):
            to_flag.append((i-1, j))
        if val == board[i+1][j] and val != int(1e9):
            to_flag.append((i+1, j))

    if val == board[i][(j-1)%m] and val != int(1e9):
        to_flag.append((i,(j-1)%m))

    if val == board[i][(j+1)%m] and val != int(1e9):
        to_flag.append((i,(j + 1) % m))

    if len(to_flag):
        to_flag.extend([(i,j)])

    return to_flag

for x,d,k in t_list:
    #회전 함시키고
    turn(x,d,k)
    #인접하면서 수가 같은것을 모두 찾는다.
    to_flag = []
    for i in range(1,n+1):
        for j in range(m):
            #인접하면서 같은 수를 모두 지운다.
            #인접하면서 같은 수가 있다면 True
            to_flag.extend(check(i,j))

    if len(to_flag):
        for xy in to_flag:
            board[xy[0]][xy[1]] = int(1e9)
    else:
        sum_of_board=0
        cnt = 0
        for i in range(1,n+1):
            for j in range(m):
                if board[i][j] != int(1e9):
                    cnt +=1
                    sum_of_board += board[i][j]
        if cnt >=1:
            avg = sum_of_board/cnt
            for i in range(1,n+1):
                for j in range(m):
                    if board[i][j] != int(1e9) and board[i][j] > avg:
                        board[i][j] -=1
                    elif board[i][j] != int(1e9) and board[i][j] < avg:
                        board[i][j] +=1

result=0
for i in range(1,n+1):
    for j in range(m):
        if board[i][j] != int(1e9):
            result += board[i][j]
print(result)