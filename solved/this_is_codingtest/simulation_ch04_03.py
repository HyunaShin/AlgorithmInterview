# -*- coding:utf8 -*-

def main(size_x,size_y, location_x, location_y, rotation, _map):
    rotation_info = [(0,-1), (1,0),(0,1),(-1,0)]
    # location_now = []
    # rotation_now = rotation_info[rotation]

    move_cnt = _map[location_x][location_y]
    _map[location_x][location_y] = 1
    def available(rotation):
        is_available = 0
        #지금 위치기준 반시계 방향으로 돌면서
        for rotate in range(1,5):
            # print(rotate)
            rotated = rotation - rotate
            print(rotated)
            #dx, dy 구함 (이동 예정인 스텝)
            dx = rotation_info[rotated][0]
            dy = rotation_info[rotated][1]
            #이동이 가능하다면
            if location_x+dx >=0 and location_y + dy >=0 and location_x + dx <= size_x and location_y + dy <= size_y:
                #지도에서 1인지 확인하고
                if _map[location_x + dx][location_y + dy] != 1:
                    #아니면 가능함에 마킹
                    is_available +=1
                    print(location_x, location_y)
                    print(dx, dy)
                    print(location_x + dx, location_y + dy)
        print(is_available)
        return is_available


    while available(rotation):
        print("running")
        for rotate in range(0,4):
            rotated = rotation - rotate
            #dx, dy 구함 (이동 예정인 스텝)
            dx = rotation_info[rotated][0]
            dy = rotation_info[rotated][1]
            #이동이 가능하다면
            if location_x+dx >=0 and location_y + dy >=0 and location_x + dx <= size_x and location_y + dy <= size_y:
                #지도에서 바다 or 방문한 곳인지 확인
                if _map[location_x + dx][location_y + dy] != 1:
                    #현재 바라보는 방향 갱신
                    rotation = rotated
                    #캐릭터 이동
                    location_x = location_x + dx
                    location_y = location_y + dy
                    #방문 했다고 마킹
                    _map[location_x][location_y] = 1
                    #이동한 수 갱신
                    move_cnt +=1

    return move_cnt


if __name__ == "__main__":
    size_y, size_x = list(map(int, input().split(" ")))
    location_y, location_x, rotation =  list(map(int, input().split(" ")))
    _map = []
    for _ in range(size_y):
        _map.append(list(map(int, input().split(" "))))

    main(size_x, size_y, location_x, location_y, rotation, _map)
    # position = input()
    # ret = main(position)
    # print(ret)