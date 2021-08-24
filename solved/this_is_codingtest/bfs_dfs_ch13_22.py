from collections import deque


def bfs(robot):
    head = robot[0]
    tail = robot[1]
    move_cnt = robot[2]
    q = deque()
    q.append((head, tail, move_cnt))

    while q:
        head, tail = q.popleft()
        head_x = head[0]
        head_y = head[1]
        tail_x = tail[0]
        tail_y = tail[1]

        for i in range(4):
            n_head_x = head_x + dx[i]
            n_head_y = head_y + dy[i]
            n_tail_x = tail_x + dx[i]
            n_tail_y = tail_y + dy[i]

            if 0 <= n_head_x < board_size and 0 <= n_head_y < board_size and 0 <= n_tail_x < board_size and 0 <= n_tail_y < board_size:
                if board[n_head_x][n_head_y] != 1 and board[n_tail_x][n_tail_y] != 1:
                    q.append(((n_head_x, n_head_y), (n_tail_x, n_tail_y), move_cnt + 1))

                # head쪽 막힘
                elif board[n_head_x][n_head_y] == 1 and board[n_tail_x][n_tail_y] != 1:
                    # head_x, head_y, tail_x, tail_y에 대해
                    # head 우상
                    ru = (head_x + corner_x[0], head_y + corner_y[0])
                    if board[ru[0]][ru[1]] != 1:
                        q.append(ru, move_cnt + 1)
                    # head 우하
                    rd = (head_x + corner_x[1], head_y + corner_y[1])
                    if board[rd[0]][rd[1]] != 1:
                        q.append(rd, move_cnt + 1)
                    # tail 좌상
                    lu = (tail_x + corner_x[2], head_y + corner_y[2])
                    if board[lu[0]][lu[1]] != 1:
                        q.append(lu, move_cnt + 1)
                    # tail 좌하
                    ld = (tail_x + corner_x[3], head_y + corner_y[3])
                    if board[ld[0]][ld[1]] != 1:
                        q.append(ld, move_cnt + 1)

                # tail쪽 막힘
                elif board[n_head_x][n_head_y] != 1 and board[n_tail_x][n_tail_y] == 1:
                    # head 우상
                    ru = (head_x + corner_x[0], head_y + corner_y[0])
                    if board[ru[0]][ru[1]] != 1:
                        q.append(ru, move_cnt + 1)
                    # head 우하
                    rd = (head_x + corner_x[1], head_y + corner_y[1])
                    if board[rd[0]][rd[1]] != 1:
                        q.append(rd, move_cnt + 1)
                    # tail 좌상
                    lu = (tail_x + corner_x[2], head_y + corner_y[2])
                    if board[lu[0]][lu[1]] != 1:
                        q.append(lu, move_cnt + 1)
                    # tail 좌하
                    ld = (tail_x + corner_x[3], head_y + corner_y[3])
                    if board[ld[0]][ld[1]] != 1:
                        q.append(ld, move_cnt + 1)

    return q


def solution(board):
    board_size = len(board)

    #####상 하 좌 우
    # 통으로 옮긴다
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    ########우상 우하 좌상 좌하
    # 대가리 떼는 케이스, 꼬리 뗴는 케이스로 나눈다
    # 벽을 만나면 돌린다
    cornerx = [-1, 1, -1, 1]
    cornery = [1, 1, -1, -1]

    robot = [(0, 0), (0, 1), 0]
    ans = bfs(robot)

    # answer =
    return ams.popleft()[-1] + 1

