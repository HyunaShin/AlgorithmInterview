from pprint import pprint
n,k = map(int, input().split())
board = [[0] * (n+1)]
board += [[0]+ list(map(int, input().split())) for _ in range(n)]

move_info  = [[[] for _ in range(n+1)] for _ in range(n+1)]
hdic = {k+1 : v for k,v in enumerate(list(map(int, input().split())) for _ in range(k))}
dx, dy = [0,0,0,-1,1],[0, 1, -1, 0, 0]
pprint(board)
for i in hdic.keys():
    x,y,dir = hdic[i]
    move_info[x][y].append((i,dir))

def move(horse_idx):
    global move_info
    x,y,dir = hdic[horse_idx]
    nx, ny = x + dx[dir], y + dy[dir]
    # print(horse_idx, hdic[horse_idx], nx,ny, board[nx][ny])
    if 0 <= nx < n and 0 <= ny < n:
        if len(move_info[x][y]):
            a_idx = move_info[x][y].index((horse_idx, dir))
        else:
            a_idx =0

        if board[nx][ny] == 0:
            #흰색인 경우 그 칸으로 가고, 이동하려는 칸에 말이 있으면 가장 위에 A번 말 올려두기
            # A번 말 위에 다른 말이 있으면, A번말과 위에 있는 모든 말이 이동
            move_info[nx][ny].extend(move_info[x][y][a_idx:])
            move_info[x][y] = move_info[x][y][:a_idx]
            for h_info in move_info[nx][ny]:
                h_idx, h_dir = h_info
                hdic[h_idx] = [nx, ny, h_dir]

        elif board[nx][ny] == 1:
            tmp = move_info[x][y][a_idx:]
            tmp.reverse()
            move_info[nx][ny].extend(tmp)
            move_info[x][y] = move_info[x][y][:a_idx]
            for h_info in move_info[nx][ny]:
                h_idx, h_dir = h_info
                hdic[h_idx] = [nx, ny, h_dir]

        elif board[nx][ny] == 2:
            # print("fourth1 : ", nx, ny, horse_idx,hdic)
            if dir == 1:
                ndir = 2
            elif dir == 2:
                ndir = 1
            elif dir == 3:
                ndir=4
            else:
                ndir = 3
            # nx, ny = x + dx[ndir], y + dy[ndir]
            # # if board[nx][ny] == 2:
            #
            #     # idx_mv = move_info[x][y].index((horse_idx, dir))
            #     # move_info[x][y][idx_mv] = (horse_idx, ndir)
            #     # hdic[horse_idx] = [nx, ny, ndir]
            # if board[nx][ny] == 0:
            #     # 흰색인 경우 그 칸으로 가고, 이동하려는 칸에 말이 있으면 가장 위에 A번 말 올려두기
            #     # A번 말 위에 다른 말이 있으면, A번말과 위에 있는 모든 말이 이동
            #     move_info[nx][ny].extend(move_info[x][y][a_idx:])
            #     move_info[x][y] = move_info[x][y][:a_idx]
            #     for h_info in move_info[nx][ny]:
            #         h_idx, h_dir = h_info
            #         hdic[h_idx] = [nx, ny, h_dir]
            #
            # elif board[nx][ny] == 1:
            #     tmp = move_info[x][y][a_idx:]
            #     tmp.reverse()
            #     move_info[nx][ny].extend(tmp)
            #     move_info[x][y] = move_info[x][y][:a_idx]
            #     for h_info in move_info[nx][ny]:
            #         h_idx, h_dir = h_info
            #         hdic[h_idx] = [nx, ny, h_dir]
            # else:
            #     idx_mv = move_info[x][y].index((horse_idx, dir))
            #     move_info[x][y][idx_mv] = (horse_idx, ndir)
            #     hdic[horse_idx] = [x, y, ndir]
            #
            # if len(move_info[nx][ny]) == 4:
            #     return False
        # else:
        # elif board[x][y] == 2:
    # else:
    #     print("fourth 2: ", nx, ny, horse_idx,hdic)
    #     if dir == 1:
    #         ndir = 2
    #     elif dir == 2:
    #         ndir = 1
    #     elif dir == 3:
    #         ndir=4
    #     else:
    #         ndir = 3
    #     idx_mv = move_info[x][y].index((horse_idx, dir))
    #     move_info[x][y][idx_mv] = (horse_idx, ndir)
    #     hdic[horse_idx] = [x, y, ndir]
        # nx, ny = x + dx[ndir], y + dy[ndir]

        # if board[nx][ny] == 2:
        #     idx_mv = move_info[x][y].index((horse_idx, dir))
        #     move_info[x][y][idx_mv] = (horse_idx, ndir)
        #     hdic[horse_idx] = [nx, ny, ndir]
        #     if board[nx][ny] == 0:
        #         # 흰색인 경우 그 칸으로 가고, 이동하려는 칸에 말이 있으면 가장 위에 A번 말 올려두기
        #         # A번 말 위에 다른 말이 있으면, A번말과 위에 있는 모든 말이 이동
        #         move_info[nx][ny].extend(move_info[x][y][a_idx:])
        #         move_info[x][y] = move_info[x][y][:a_idx]
        #         for h_info in move_info[nx][ny]:
        #             h_idx, h_dir = h_info
        #             hdic[h_idx] = [nx, ny, h_dir]
        #
        #     elif board[nx][ny] == 1:
        #         tmp = move_info[x][y][a_idx:]
        #         tmp.reverse()
        #         move_info[nx][ny].extend(tmp)
        #         move_info[x][y] = move_info[x][y][:a_idx]
        #         for h_info in move_info[nx][ny]:
        #             h_idx, h_dir = h_info
        #             hdic[h_idx] = [nx, ny, h_dir]

        # else:
        #     print("else", nx, ny, horse_idx)

    return None

turn = 0
while turn < 1000:
    for i in range(1,5):
        ret = move(i)
        # print(hdic)
        pprint(move_info)
        print(ret)
    exit()
    # print(move_info)
    # print(hdic)
    # exit()
    #     if ret == False:
    #         print(turn)
    # turn +=1
    # # print(turn)
    # if turn ==2:
    #     print(move_info)
        # print(move_info)
    #     # turn +=1

if turn >= 1000:
    print(-1)
