from pprint import pprint
# board = [[0] * 4 for _ in range(4)]
gboard = [[0]* 4 for _ in range(6)]
bboard = [[0]* 6 for _ in range(4)]
# pprint(gboard)
# print(len(gboard), len(gboard[0]))
# print()
# pprint(bboard)
# print(len(bboard), len(bboard[0]))
'''
4
1 1 1
2 3 0
3 2 2
3 2 3
'''
special = [0,1]
def blue(x,y):
    nx, ny = x , y+1
    while True:
        # print(nx, ny, bboard[nx][ny])
        if ny < 5 and bboard[nx][ny] !=0 :
            return nx, ny-1
        elif ny >=5:
            if bboard[nx][ny] !=0 :
                return nx, ny-1
            else:
                return nx, ny
        ny +=1

def green(x,y):
    nx, ny = x +1,  y
    while True:
        if nx < 5 and gboard[nx][ny] !=0:
            return nx-1, y
        elif nx >= 5:
            if gboard[nx][ny] !=0:
                return nx-1, ny
            else:
                return nx, ny
        nx += 1

for i in range(int(input())):
    score = 0
    t,x,y = map(int, input().split())
    if t ==1:
        bx, by = blue(x,y)
        gx, gy = green(x,y)
        bboard[bx][by] = 1
        gboard[gx][gy] = 1


    elif t == 2:
        from pprint import pprint
        #blue는 그냥 가면 되고
        bax, bay = blue(x,y)
        bboard[bax][bay] = 2
        # print(bax, bay, bbx, bby)
        # print(bboard[0])
        # print(bboard[1])
        # print(bboard[2])
        # print(bboard[3])
        # exit()
        # print(bboard)
        # exit()
        bbx, bby = blue(x,y+1)
        bboard[bbx][bby] = 2
        # print("""here""")
        # print(bboard[0])
        # print(bboard[1])
        # print(bboard[2])
        # print(bboard[3])
        # print("""here""")

        # pprint(bboard)
        # print(bax, bay, bbx, bby)

        # exit()
        # print(bax,bay,bbx, bby)

        #green은  x에 튀어나온 놈이 있을 수도 있음.
        gax, gay = green(x,y)
        gboard[gax][gay] = 2
        gbx, gby = green(x,y+1)
        gboard[gbx][gby] = 2
        gx = min(gax, gbx)
        gboard[gx][gby] = 2
        if gx == gbx:
            gboard[gax][gay] = 0
            gboard[gx][gay] = 2

        # print(gboard[0])
        # print(gboard[1])
        # print(gboard[2])
        # print(gboard[3])
        # print(gboard[4])
        # print(gboard[5])
        # print(gx, gbx, gby, gax, gay)
        # exit()

    else:

        #y에 튀어나온놈 나올수도 있음
        bax, bay = blue(x,y)
        bboard[bax][bay] = 3

        bbx, bby = blue(x+1,y)
        by = min(bay, bby)
        bboard[bbx][by] = 3

        if by == bby:
            # print(bax, bay, bbx, bby)
            bboard[bax][bay] = 0
            bboard[bax][by] = 3
            # print(bax,bay, bax, by)
            # print(bboard[0])
            # print(bboard[1])
            # print(bboard[2])
            # print(bboard[3])
            # exit()
        print(x,y, bax, bay, bbx, bby)
        #그냥 가면됨
        gax, gay = green(x,y)
        gboard[gax][gay] = 3
        gbx, gby = green(x+1,y)
        gboard[gbx][gby] = 3

    # #그럼 0,1번에 대한 파랑, 초록에서 처리를 한번 해줘야겠네
    # #초록
    # h_remove = []    #지울 행의 수
    # for i in range(2):
    #     for j in range(4):
    #         if gboard[i][j] != 0:
    #             # print("hremoving")
    #             h_remove.append(i)
    #
    # if len(h_remove):
    #     score += len(h_remove)
    #     #블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고,
    #     for i in range(6, 6-len(h_remove), -1):
    #         gboard[i][:] = [0] * 4
    #     #  초록색 보드의 모든 블록이 사라진 행의 수만큼 아래로 이동
    #     for i in range(6, len(h_remove), -1):
    #         gboard[i][:] = gboard[i-len(h_remove)][:]
    #
    # # 초록 : 행이 꽉 차면 지우게하기
    # removed_x = []
    # for i in range(5, 0, -1):
    #     to_remove = []
    #     for j in range(4):
    #         if gboard[i][j] != 0:
    #             to_remove.append((i,j))
    #
    #     if len(to_remove) == 4:
    #         removed_x.append(i)
    #
    # for i in removed_x:
    #     gboard[i] = [0] * 4
    #     gboard[i-1][:] = gboard[i][:]
    #     score += 1
    #
    # #파랑
    # v_remove = []    #지울 열의 수
    # for j in range(2):
    #     for i in range(4):
    #         if bboard[i][j] != 0:
    #             v_remove.append(j)
    #
    # if len(v_remove):
    #     score += len(v_remove)
    #     #블록이 있는 열의 수만큼 뒷열에 있는 타일이 사라지고,
    #     for j in range(5,  5-len(v_remove), -1):
    #         for i in range(4):
    #             bboard[i][j] = 0
    #
    #     #  파란색 보드의 모든 블록이 사라진 열의 수만큼 뒤로 이동
    #     for j in range(6, len(v_remove), -1):
    #         for i in range(4):
    #             bboard[i][j] = bboard[i][j-len(v_remove)]
    #
    # # 파랑 : 열이 꽉 차면 지우게하기
    # removed_y = []
    # for j in range(5,0,-1):
    #     to_remove = []
    #     for i in range(4):
    #         if bboard[i][j] != 0:
    #             to_remove.append((i,j))
    #
    #     if len(to_remove) == 4:
    #         removed_y.append(j)
    #
    # for j in removed_y:
    #     score += 1
    #     for i in range(4):
    #         bboard[i][j] = bboard[i][j-1]

    print(bboard[0])
    print(bboard[1])
    print(bboard[2])
    print(bboard[3])
    print()
    print(gboard[0])
    print(gboard[1])
    print(gboard[2])
    print(gboard[3])
    print(gboard[4])
    print(gboard[5])

    print()

    #
kan = 0
for i in bboard:
    for j in i:
        if j != 0:
            kan +=1

for i in gboard:
    for j in i:
        if j != 0:
            kan +=1

print(score)
print(kan)