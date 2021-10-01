def dirt():
    #확산되는 미세먼지
    dirt_tbl = [[[] for _ in range(c)]  for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] != -1:
                to_move = int(board[x][y]/5)
                move_cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        dirt_tbl[nx][ny].append((to_move))
                        move_cnt +=1
                to_reserve = board[x][y] - (to_move * move_cnt)
                #남은 미세먼지
                board[x][y] = to_reserve

    #확산 된 미세먼지의 sum을 남은량에 더해준다(모아서 업데이트)
    for x in range(r):
        for y in range(c):
            if board[x][y] != -1:
                board[x][y] += sum(dirt_tbl[x][y])


def clean(head, tail):
    hx, hy = head
    tx, ty = tail
    ###시계방향
    board[hx-1][0] = 0
    for i in range(hx-1, 0,-1): #하향
        board[i][0]= board[i-1][0]
    board[0][0] = 0

    for i in range(1,c): #좌향
        board[0][i-1] = board[0][i]
    board[0][c-1] = 0

    for i in range(0,hx): #상향
        board[i][c-1] = board[i+1][c-1]
    board[hx][c-1] = 0

    for i in range(c-1,1,-1): #우향
        board[hx][i] = board[hx][i-1]
    board[hx][1] = 0

    #####반시계방향
    board[tx+1][0] = 0
    for i in range(tx+1, r-1): #상향
        board[i][0]= board[i+1][0]
    board[r-1][0] = 0

    for i in range(1,c): #좌향
        board[r-1][i-1] = board[r-1][i]
    board[r-1][c-1] = 0


    for i in range(r-1,tx, -1): #하향
        board[i][c-1] = board[i-1][c-1]
    board[tx][c-1] = 0

    for i in range(c-1,1, -1): #우향
        board[tx][i] = board[tx][i-1]
    board[tx][1]=0



if __name__ == "__main__":
    r,c,t = map(int, input().split())
    board= []
    cleaners = []
    dx,dy = [-1,0,1,0], [0,1,0,-1]
    for i in range(r):
        board.append(list(map(int, input().split())))
        if board[i][0] == -1:
            cleaners.append((i,0))

    for _ in range(t):
        dirt()
        clean(cleaners[0],cleaners[1])

    result = 2
    for i in range(r):
        result += sum(board[i])

    print(result)


