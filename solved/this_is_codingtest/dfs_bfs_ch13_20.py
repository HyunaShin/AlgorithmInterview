#========================복기===================
from itertools import combinations

def watch(x,y,direction):
    '''
    direction
    0 : 상, 1 : 하, 2 : 좌, 3 :우
    '''
    if direction == 0:
        while x >= 0:
            if graphs[x][y] == "S":
                return True
            elif graphs[x][y] == "O":
                return False
            x -= 1
    elif direction == 1:
        while x < n:
            if graphs[x][y] == "S":
                return True
            elif graphs[x][y] == "O":
                return False
            x += 1
    elif direction == 2:
        while y >= 0:
            if graphs[x][y] == "S":
                return True
            elif graphs[x][y] == "O":
                return False
            y -= 1
    else:
        while y < n:
            if graphs[x][y] == "S":
                return True
            elif graphs[x][y] == "O":
                return False
            y += 1
    return False

if __name__ == "__main__":
    n = int(input())
    stairs = []
    teachers = []
    graphs = []
    for i in range(n):
        graphs.append(input().split(" "))
        for j in range(n):
            if graphs[i][j] == "T":
                teachers.append((i,j))
            elif graphs[i][j] == "X":
                stairs.append((i,j))

    students = []
    #벽 세우기
    for wall_info in combinations(stairs,3):
        #벽세우기
        for i,j in wall_info:
            graphs[i][j] = "O"

        #선생님마다
        student_cnt = 0
        for x,y in teachers:
            #상하좌우로 감시하기
            for direction in range(4):
                #감시해서 해당 방향으로 지켜봤을 때 학생 있는지
                student_cnt += watch(x,y,direction)
        #벽 세웠고, 지켜봤을떄 감지된 학생 수
        students.append(student_cnt)

    no_student = False
    for i in students:
        if i == 0:
            no_student = True
            print("YES")
            break

    if not no_student:
        print("NO")


#========================원본===================

from itertools import combinations

def dfs(x,y,direction):
    global student_cnt
    dx, dy = direction_info.get(direction)
    for i in range(4):
        nx = x+dx
        ny = y+dy
        if nx >=0 and nx < n and ny >=0 and ny < n:
            if wall_info[nx][ny] == 'X':
                wall_info[nx][ny] = 'T'
                dfs(nx, ny, direction)
            elif wall_info[nx][ny] == "S":
                student_cnt -=1
                wall_info[nx][ny] = 'T'

                dfs(nx, ny, direction)

    return

def main():
    global wall_info
    global student_info
    map_list= []
    for i in range(n):
        for j in range(n):
            map_list.append((i,j))

    for wall in combinations(map_list,3):
        student_cnt = len(student_info)
        wall_info = [x for x in stair_info]
        wall_info[wall[0][0]][wall[0][1]] = "O"
        wall_info[wall[1][0]][wall[1][1]] = "O"
        wall_info[wall[2][0]][wall[2][1]] = "O"
        for x, y, direction in teacher_info:
            dfs(x,y,direction)


if __name__ == "__main__":
    n = int(input())
    stair_info = []

    for i in range(n):
        stair_info.append(input().split())

    direction_info = {'u': (-1,0), "d" : (1,0), 'l' : (0,-1), 'r' : (0,1)}
    teacher_info = []
    student_info = []
    student_cnt = len(student_info)

    for i in range(n):
        for j in range(n):
            if stair_info[i][j] == "T":
                for k in range(4):
                    teacher_info.append((i,j,list(direction_info.keys())[k]))
            elif stair_info[i][j] == "S":
                student_info.append((i,j))
    main()

    if student_cnt == len(student_info):
        print("YES")
    else:
        print("NO")