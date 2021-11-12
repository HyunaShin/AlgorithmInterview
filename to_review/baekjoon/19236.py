def main():
    from collections import deque
    import copy

    fish_list = [0] * 17
    board = [[0] * 4  for _ in range(4)]
    dx,dy=[0,-1,-1,0,1,1,1,0,-1],[0,0,-1,-1,-1,0,1,1,1]

    for i in range(4):
        tmp = list(map(int, input().split()))
        #보드 초기화
        for j in range(4):
            board[i][j] = [tmp[(j*2)], tmp[(j*2)+1]]
            fish_list[tmp[j*2]] = [i,j]

    def mv_fish(b, sx, sy, fish):
        tmp = copy.deepcopy(fish)
        for i, (x,y) in enumerate(fish[1:]):
            if b[x][y][1] != -1:
                "내가 먹힌 물고기가 아니라면"
                dir = b[x][y][1]
                nx, ny = x + dx[dir], y + dy[dir]
                if 0 <= nx < 4 and 0 <= ny < 4 and (nx,ny) != (sx,sy):
                    tmp[b[x][y][0]], tmp[b[nx][ny][0]] = tmp[b[nx][ny][0]], tmp[b[x][y][0]]
                    b[x][y], b[nx][ny] =b[nx][ny], b[x][y]
                    # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
                else:
                    ndx = dx[dir:] + dx[:dir]
                    ndy = dy[dir:] + dy[:dir]
                    for k in range(8):
                        nx, ny = x + ndx[k], y + ndy[k]
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            if (nx,ny) != (sx,sy):
                                tmp[b[x][y][0]], tmp[b[nx][ny][0]] = tmp[b[nx][ny][0]], tmp[b[x][y][0]]
                                b[x][y], b[nx][ny] = b[nx][ny], b[x][y]
                                b[nx][ny] = [b[nx][ny][0],(dir+k)%8]
                                break
        return b, tmp

    result = 0
    q = deque()
    #x, y, 방향 , 보드, 스코어
    q.append((0,0,board[0][0][1], board, 0, fish_list))
    # print(board[0])
    # print(board[1])
    # print(board[2])
    # print(board[3])
    while q :
        x, y, dir, bb, score,fish = q.popleft()
        number = bb[x][y][0]
        bb[x][y][1] =-1 #먹었다는 처리. 확인 필요
        bb, fish = mv_fish(bb, x,y, fish)
        # exit()
        result = max(score+number, result)
        for _ in range(1,4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4 and bb[nx][ny][1] != -1:
                q.append((nx, ny, bb[nx][ny][1], bb, score+number,fish))
            x,y = nx, ny
        # else:

            # result = max(score, result)

    print(result)
    return

answer=0
def solution():
    '''
    상어가 갈 수 있는 자리가 여러 곳인데, 상어의 위치를 옮기면 그때마다 물고기의 위치도
    다 달라지기 때문에 dfs로 풀어야 한다.
    그리고 번호가 높다고 최종적으로 최댓값이 된다는 보장이 없다.
    모든 경우에 대해 끝까지 진행하고 최종적으로 판단해야한다.
    1. 현재 상어 위치에 있는 물고기를 먹는다.
    2. 모든 물고기를 이동 시킨다.
    3. 상어가 먹을수 있는 물고기를파악한다.
    4. 3번의 모든 경우에 대해서 dfs탐색을 진행한다.
    '''

    import copy
    dx, dy = [ -1, -1, 0, 1, 1, 1, 0, -1], [ 0, -1, -1, -1, 0, 1, 1, 1]
    #상어가 먹을 수 있는 후보 위치 반환
    def food(array, x, y):
        positions = []
        direction = array[x][y][1]
        for i in range(1,4):
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny][0] <= 16:
                positions.append([nx,ny])
            x,y = nx, ny
        return positions

    #현재 배열에서 특정한 번호의 물고기 찾기
    def find_fish(array, index):
        for i in range(4):
            for j in range(4):
                if array[i][j][0] == index:
                    return (i,j)
        return None

    def move_fish(array, now_x, now_y):
        flag = False
        position = []
        for i in range(1,17):
            position =find_fish(array,i)
            if position is None:
                continue
            x,y = position[0], position[1]
            dir = array[x][y][1]#방향
            for j in range(8):
                #돌려보면서
                nx, ny = x + dx[dir], y + dy[dir]
                # 공간에 경계 안에 있는지 체크
                if 0 <= nx < 4 and 0<= ny < 4:
                    #상어있는칸인지 체크
                    if not (nx == now_x, ny ==now_y):
                        array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                        array[x][y][1], array[nx][ny][1] = array[nx][ny][1], dir
                        break
                dir = (dir+1)%8
        return

    def dfs(array, x, y, total):
        global answer
        array = copy.deepcopy(array)
        #해당 위치 물고기 먹기
        number = array[x][y][0]
        #물고기 이동
        move_fish(array, x, y)
        #상어가 이동할 수 있는 후보 확인
        result = food(array, x, y)

        #해당 먹이를 찾는 모든 과정 탐색
        answer = max(answer, total + number)
        for next_x, next_y in result:
            dfs(array, next_x, next_y, total + number)



    temp = [list(map(int, input().split() ))for _ in range(4)]
    array = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            array[i][j] = [temp[i][j*2], temp[i][j*2+1]-1 ]

    answer = 0
    dfs(array, 0,0,0)
    print(answer)
if __name__ == "__main__":
    main()
    # solution()

