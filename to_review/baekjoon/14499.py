def main():
    from collections import deque
    n,m,x,y,k = map(int, input().split())
    #O(NM)
    graph =[]
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    #O(K)
    #동쪽은 1, 서쪽은2, 북쪽은 3, 남쪽은 4로 이동 명령이 주어진다.
    commands = deque(list(map(int, input().split())))
    #남, 동, 북, 서 순으로 움직인다.
    dx, dy = [0,0,0,-1,1 ],[0,1,-1,0,0 ]
    #주사위의 상태값
    dice = [0] * 7
    bottom = 6
    # 동쪽은 1, 서쪽은2, 북쪽은 3, 남쪽은 4
    dice_info = {1 : [1,3,4,2,5,6], 2 : [2,3,4,6,1,5],
                 3 : [3,6,1,2,5,4], 4: [4,1,6,2,5,3],
                 5 : [5,3,4,1,6,2], 6:[6,3,4,5,2,1]}
    def run_dice(command, bottom):
        '''주사위를 던지는 메소드, 몇번째 주사위 인덱스에 접근할지'''
        if command ==1:
            dice_info[bottom][1:5] = [dice_info[bottom][4], dice_info[bottom][3],dice_info[bottom][2], dice_info[bottom][1]]

            tb = dice_info[bottom][3]
            dice_info[tb][1:5] = [dice_info[tb][4], dice_info[tb][3], dice_info[tb][2],dice_info[tb][1]]

            tb = dice_info[bottom][4]
            dice_info[tb][1:5] = [dice_info[tb][4], dice_info[tb][3], dice_info[tb][2], dice_info[tb][1]]

            tb = dice_info[bottom][5]
            dice_info[tb][1:5] = [dice_info[tb][4], dice_info[tb][3], dice_info[tb][2], dice_info[tb][1]]


        elif command == 2:
            dice_info[bottom][1:5] = [dice_info[bottom][4], dice_info[bottom][3],dice_info[bottom][1], dice_info[bottom][2]]
            tb = dice_info[bottom][3]
            dice_info[tb][1:5] =  [dice_info[tb][4], dice_info[tb][3],dice_info[tb][1], dice_info[tb][2]]

            tb = dice_info[bottom][4]
            dice_info[tb][1:5] =  [dice_info[tb][4], dice_info[tb][3],dice_info[tb][1], dice_info[tb][2]]

            tb = dice_info[bottom][5]
            dice_info[tb][1:5] =  [dice_info[tb][4], dice_info[tb][3],dice_info[tb][1], dice_info[tb][2]]

        return dice_info[bottom][command]


    def copy_value(nx,ny,nb):
        '''주사위의 밑면과 지도의 값을 복사하는 메소드'''
        global graph, dice
        # print(graph, nx, ny,graph[nx][ny], nb)
        # 이동한 칸에 쓰인 수가 0이면 주사위 바닥면의 수가 칸에 복사
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[nb]
        else:
            dice[nb] = graph[nx][ny]
            graph[nx][ny] = 0

    def main(command, x,y):
        '''주사위를 이동하는 메소드'''
        global bottom
        #굴렸더니 바닥에 있는 번호(몇번째 인덱스인지)
        nb = run_dice(command, bottom)
        # 굴렸을때 갈 위치
        nx,ny = x + dx[command], y + dy[command]
        if 0 <= nx < n and 0 <= ny < n:
            copy_value(nx, ny, nb)
            #밑면에 있는 값 복사 했고, 이동 끝났으니까 상단에 쓰인 값 찾기
            print(dice[dice_info[bottom][-1]])
            bottom = nb
            return nx, ny
        return x,y

    while commands:
        command = commands.popleft()
        # print(command)
        x,y = main(command, x,y)
    return None

def solution():
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    n,m,x,y,k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    #명령 k개
    order = list(map(int, input().split()))
    dice = [0 for _ in range(6)]

    for i in range(k):
        #굴릴 방향
        dir = order[i] -1
        #동,서,북,남
        nx = x + dx[dir]
        ny = y + dy[dir]
        #그래프 범위 안일때
        if not 0 <= nx < n or not 0 <= ny < m:
            continue

        if dir == 0:
            #동쪽으로 굴릴 경우 바뀌는 면들
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif dir == 1:
            #서쪽으로 굴릴 경우 바뀌는 면들
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif dir ==2:
            #북쪽으로 굴릴 경우 바뀌는 면들
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        elif dir == 3:
            #남쪽으로 굴릴 경우 바뀌는 면들
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        #현재칸이 0이면 주사위 아랫면의 숫자로 바꿔준다.
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[5]
        #0이 아니면 칸의숫자를 주사위 아랫면으로 옮겨우고 칸의 숫자를 0으로 바꿔준다
        else:
            dice[5] = graph[nx][ny]
            graph[nx][ny] =0
        x,y = nx, ny
        print(dice[0])
    return