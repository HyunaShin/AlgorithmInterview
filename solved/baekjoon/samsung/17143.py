from pprint import pprint
def move():
    #보드에 반영할 좌표와 상어
    move_result = dict()
    #변경된 상어 정보
    shark_result = []
    for x,y,size in shark.keys():
        #상어를 이동시킨다.
        ss,sd = shark[(x,y,size)]
        origin_info = (x,y,ss,sd,size)
        cnt = 0
        while cnt < ss:
            # print(x,y,cnt,ss,sd,cnt)
            nx,ny = x+dx[sd], y + dy[sd]
            if 0<= nx < r and 0 <= ny < c:
                x,y = nx, ny
                cnt += 1
            elif sd == 1 and nx == -1: #위
                sd = 2
                x,y  = x + dx[sd], y + dy[sd]
                cnt += 1
            elif sd == 2 and nx == r: #아래
                sd = 1
                x,y = x + dx[sd], y + dy[sd]
                cnt += 1

            elif sd ==3 and ny == c: #오
                sd=4
                x,y = x + dx[sd], y + dy[sd]
                cnt += 1

            elif sd ==4 and ny ==-1: #왼
                sd =3
                x,y = x + dx[sd], y + dy[sd]
                cnt += 1

        if not move_result.get((x,y)):
            move_result[(x,y)] = [size]
        else:
            move_result[(x,y)].append(size)

        # 상어의 출발, 도착 반영
        shark_result.append((origin_info, (x, y, ss,sd,size)))
    return move_result, shark_result

if __name__ =="__main__":
    #d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
    dx = [0,-1,1,0,0]
    dy = [0,0,0,1,-1]
    r,c,m = map(int,input().split())
    board = [[0] * c for _ in range(r)]
    # print(board)
    shark = dict()
    for i in range(m):
        # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다.
        #두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
        sr, sc, s, d, z = map(int,input().split())
        # print(sr,sc,z)
        # (x, y, ss, sd, size)
        shark[(sr-1,sc-1,z)] = (s,d)
        board[sr-1][sc-1] = z

    result = 0
    for col in range(c):
        for row in range(r):
    # for row in range(r):
    #     for col in range(c):
            #1초간 일어나는 일
            #상어가 있으면 잡는다. 맨 처음에는 최대 한마리가 주어진다.
            if board[row][col] != 0:
                #상어 잡기
                size = board[row][col]
                board[row][col] = 0
                result += size
                # 상어를 잡은 경우, 상어 목록에서도 제거 시킴
                if shark.get((row,col,size)):
                    shark.pop((row,col,size))

                #상어를 이동시킨다.
                #이 때, 상어의 상태가 업데이트 됨.
                move_result, shark_result = move()
                print(shark_result)
                #제일 큰 상어가 같은 칸에 있는 상어를 잡아먹고
                for dir in move_result.keys():
                    max_size = max(move_result[dir])
                    move_result[dir] = max_size
                    # board[row][col] = max_size

                #상어가 이동했으니, 정보를 업데이트 해 준다.
                for _from, _to in shark_result:
                    # (x, y, ss->속도, sd->방향, size->크기)
                    # shark[(sr - 1, sc - 1, z)] = (s, d)
                    #상어 정보 갱신 - 기존 정보 비우고
                    shark.pop((_from[0], _from[1], _from[-1]))
                    board[_from[0]][_from[1]] = 0
                    #이동했을 때 살아 있다면
                    if _to[4] == move_result[(_to[0],_to[1])]:
                        #이동한 좌표를 반영한다.
                        shark[(_to[0], _to[1], _to[-1])] = (_to[2], _to[3])
                        board[_to[0]][_to[1]] = _to[-1]

                break

    print(result)
