from itertools import combinations

def watch(x,y,direction):
    '''
    특정 방향으로 감시를 진행한다.
    '''
    #왼쪽 방향으로 감시
    if direction == 0:
        while y>=0:
            if board[x][y] == "S":
                return True
            if board[x][y] == 'O':
                return False
            y-=1
    #오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            #학생이 있는 경우
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y +=1
    #위쪽 방향으로 감시
    if direction ==2:
        while x >=0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x-=1

    if direction == 3:
        while x < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x +=1
    return False

def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

if __name__ == "__main__":
    n = int(input())
    board = [] # 복도정보(N X N)
    teachers = [] # 모든 선생님 위치 정보
    spaces = [] #모든 빈 공간 위치 정보

    for i in range(n):
        board.append(list(input().split()))
        for j in range(n):
            if board[i][j] == "T":
                teachers.append((i,j))
            if board[i][j] == "X":
                spaces.append((i,j))
    find = False

    for data in combinations(spaces, 3):
        for x,y in data:
            board[x][y] = 'O'
        #학생을 발견하지 못한 경우
        if not process():
            #원하는 케이스 발견
            find = True
            break
        for x,y in data:
            board[x][y] = "X"

    if find:
        print("YES")
    else:
        print("NO")


