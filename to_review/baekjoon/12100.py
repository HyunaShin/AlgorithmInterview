# # def main():
# from copy import deepcopy
# n = int(input())
# #그래프
# graph = [list(map(int, input().split())) for _ in range(n)]
# #합쳐진 정보
# merged = [[False] * n  for _ in range(n)]
# visited = [[False] * n  for _ in range(n)]
# dx, dy = (1,-1,0,0),(0,0,1,-1)
# tmp = {(1,0):"d" ,(-1,0):"u", (0,1): "r", (0,-1):"l"}


# def move(graph, visited, merged, _dx, _dy, cnt, inflow):
# def move(graph, visited, merged, _dx, _dy, cnt, inflow):
#     # print(inflow)
#     if inflow[0:4] == ['u', 'r','d',"l"]:
#         print(graph, visited, merged, _dx, _dy, cnt, inflow)
#     if cnt == 5:
#         max_num = 0
#         #N^2 +3
#         for i in range(n): #N
#             for j in range(n): #N
#                 max_num = max(max_num, graph[i][j]) #3
#         return max_num
#
#
#     for _ in range(n):
#         for x in range(n):
#             for y in range(n):
#                 nx, ny = x + _dx, y + _dy
#                 visited[x][y] = True
#                 #가려는 위치가 그래프 범위 내라면
#                 if 0<= nx < n and 0 <= ny < n:
#                     #두개가 같고, 합쳐진 이력이 없다면
#                     if graph[nx][ny] == graph[x][y] and merged[nx][ny] == False and graph[x][y] != 0:
#                         #밀고
#                         graph[nx][ny] += graph[x][y]
#                         #원래칸은 빈칸으로
#                         graph[x][y] = 0
#                         merged[nx][ny] = True
#                     #두개가 다르고, 한쪽이 0이면 이동
#                     if graph[nx][ny] != graph[x][y] and graph[nx][ny] == 0:
#                         graph[nx][ny] += graph[x][y]
#                         graph[x][y] = 0
#
#     merged = [[False] * n for _ in range(n)]
#     max_num = 0
#     for i in range(4):
#         _max = move(graph, visited, merged, dx[i], dy[i], cnt + 1, inflow + [tmp[(dx[i], dy[i])]])
#         max_num = max(max_num, _max)
#     return max_num
#
#
# max_num = 0
# for i in range(4):
#     _max = move(graph, visited, merged, dx[i], dy[i], 1, [tmp[(dx[i], dy[i])]])
#     max_num = max(max_num,_max)
# print(max_num)

    # return


from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer, q, = 0 ,deque()
def get(i,j):
    '''
    원소의 값을 함 보고, 0이 아니면 옮길 후보군에 추가
    처리된 빈 자리는 0으로 업데이트.
    '''
    #0이 아닌 값이라면
    if board[i][j]:
        #queue에 board의 값을 넣는다.
        q.append(board[i][j])
        #처리가 된 빈 자리는 0으로 값 업데이트
        board[i][j] = 0


#row index, column index, y방향, x방향
def merge(i,j, di, dj):
    while q:
        #움직이려는 블록 값을 가져온다(FIFO)
        x= q.popleft()
        #0이라면 그대로 놓는다.
        #이때 i,j는 왜 증가를 안시키지?
        #아.. 다음에 올 놈이 또 지금 위치로 와도 됨
        if not board[i][j]:
            board[i][j] = x
        #값이 일치한다면
        elif board[i][j] == x:
            #합쳐지므로 2배 증가
            #다음에 올 놈은, 한스텝 뒤에 둬야함
            board[i][j] = x *2
            i,j = i + di, j +dj
        #값이 일치하지 않으면, 보고있는 위치 한스텝 뒤에 둬야지
        else:
            i,j = i+di, j + dj
            board[i][j] = x
    return

def move(k):
    '''
    상/하 -> 행 고정 열 움직임(가로 고정, 세로 움직임)
    좌/우 -> 열 고정 행 움직임(세로 고정, 가로 움직임)
    '''
    #위로 이동, 블락들이 모두 위로 이동했을 때 row index는 0
    if k == 0:
        #행 고정, 열 이동
        for j in range(n):
            #열 이동
            for i in range(n):
                #(0,0), (1,0), (2,0)
                #(0,1), (1,1), (2,1)
                #(0,2), (1,2), (2,2)
                get(i,j)
            #row index 1씩 증가하면서 아래쪽 블락들을 합쳐감
            #큐에 원래 있던 값을 넣어두고
            #떙겨와야하는 놈의 값이랑 비교해
            #
            merge(0,j,1,0)

    #아래로 이동, 블락들이 아래로 모두 이동하면 row index는 n-1
    elif k == 1:
        for j in range(n):
            for i in range(n):
                get(i,j)
            #row 인덱스 1씩 감소하면서 위쪽들을 합쳐감
            merge(n-1, j, -1, 0)
    #오른쪽으로 이동, column index는 0
    elif k == 2:
        for i in range(n):
            for j in range(n):
                get(i,j)
            merge(j,0,0,1)

    #왼쪽으로 이동, column index는 n-1
    else:
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i,j)
            #column인덱스 감소 왼쪽으로 이동
            merge(i, n-1, 0, -1)

    return

def solve(count):
    global board, answer
    #최대 5번까지 움직였다면
    if count ==5:
        for i in range(n):
            #가장 큰 값이 answer
            answer = max(answer, max(board[i]))
        return

    #원래 보드 값 카피
    b = [x[:] for x in board]
    #4방향으로 움직인다.
    for k in range(4):
        #움직인다 -> 원소 값을 큐에 넣고, 방향별로 문제 요구사항대로 합침
        move(k)
        #재귀적으로 호출한다.
        solve(count +1)
        #처리가 끝나면 원복한다.
        board = [x[:] for x in b]
solve(0)
print(answer)

# if __name__ == "__main__":
#     ans = solution()
#     print(ans)