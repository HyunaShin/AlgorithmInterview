def main():
    import copy
    n,m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    cases = {
        0: [ ("+","+",0,0), ("+","+",0,1), ("+","+",0,2), ("+","+",0,3)],
        1: [ ("+","+",0,0), ("+","+",0,1), ("+","+",1,0), ("+","+",1,1)],
        2: [("+", "+", 0, 0), ("+", "+", 1, 0), ("+", "+", 2, 0), ("+", "+", 2, 1)],
        3: [("+", "+", 0, 0), ("+", "+", 1, 0), ("+", "+", 1, 1), ("+", "+", 2, 1)],
        4: [("+", "+", 0, 0), ("+", "+", 0, 1), ("+", "+", 0, 2), ("+", "+", 1, 1)]
    }

    def turn(tetro_list, angle):
        #O(16)
        if angle == 0:
            return tetro_list

        tetro = copy.deepcopy(tetro_list)
        #90도는 더하는 축 반대
        if angle == 1:
            tetro[3],tetro[2] = tetro[2], tetro[3]
        #180도는 부호만 반대
        elif angle == 2:
            tetro[0], tetro[1] = tetro[1], tetro[0]
        #270도는 축과 부호 모두 반대
        else:
            tetro[0], tetro[1],tetro[2], tetro[3] = tetro[1], tetro[0],tetro[3], tetro[2]
        return tetro

    max_val = 0
    #x축
    for x in range(n):#O(52 * 4 * 5 * 500 * 500)
        #y축
        for y in range(m): #O(52 * 4 * 5 * 500)
            #모든 도형에 대해
            for i in range(5): #O(52 * 4 * 5)
                #한번씩 다 돌려보면서
                for j in range(4):
                    tmp_sum = 0
                    space_list = turn(cases[i], j)
                    #해당 위치한칸한칸씩 놓아서, 값의합을 본다
                    for space in space_list: #O((4 * 15)+16 = 36)
                        cnt = 0
                        nx, ny = None, None
                        if space[0] == "+":
                            nx = x + space[2]
                            cnt +=1
                        elif space[0] == "-":
                            nx = x - space[2]
                            cnt += 1

                        if space[1] == "+":
                            ny = y+space[3]
                            cnt += 1
                        elif space[1] == "-": #O(2 + 4)
                            ny = y-space[3] #O(4)
                            cnt += 1

                        if cnt ==2 and (0 <= nx < n) and (0 <= ny < m):
                            tmp_sum += graph[nx][ny]
                max_val = max(tmp_sum, max_val)

    print(max_val)
    return None

def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    tetromino = [
        [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
        [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(1, 0), (1, 1), (1, 2), (0, 2)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
        [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(2, 0), (2, 1), (1, 1), (0, 1)],
        [(0, 0), (0, 1), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
        [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
        [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
        [(1, 0), (2, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(1, 0), (0, 1), (1, 1), (0, 2)],
        [(0, 0), (0, 1), (1, 1), (1, 2)]
    ]

    def find(x, y):
        global answer
        for i in range(19):
            result = 0
            for j in range(4):
                try:
                    next_x = x + tetromino[i][j][0]  # x 좌표
                    next_y = y + tetromino[i][j][1]  # y 좌표
                    result += board[next_x][next_y]
                except IndexError:
                    continue
            answer = max(answer, result)

    def solve():
        for i in range(n):
            for j in range(m):
                find(i, j)

    answer = 0
    solve()
    print(answer)


if __name__ == "__main__":
    main()