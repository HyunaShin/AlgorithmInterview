# -*- coding:utf8 -*-
def main(position):
    x = ['a','b','c','d','e','f','g','h']
    y = [1,2,3,4,5,6,7,8]
    # RU, RD, DL, DR, LU, LD, UL, UR
    movements = [(2,-1), (2,1), (-1,2), (1,2), (-2,-1), (-2,1), (-1,-2), (1,-2)]

    dx = list(filter(lambda x : x[-1] == position[0], enumerate(x)))[0][0]
    dy = list(filter(lambda x : x[-1] == int(position[1]), enumerate(y)))[0][0]

    cases =0
    for move in movements:
        if (dx + move[0] >= 0 )and (dy + move[1] >=0) and (dx + move[0] <= 8) and (dx + move[0] <= 8):
            cases +=1

    return cases

if __name__ == "__main__":
    position = input()
    ret = main(position)
    print(ret)