#중심에 내가 있다고 치고, 움직일떄
import math
# move_info = [[(0,1), (-1,1), (1,0)],[(-1,1), (0,0), (1,1)],[(-1,0), (-1,1), (0,-1)]]

dx = [0, 1,1, 1, 0, 1,-1,-1, -1, -1]
dy = [1, 1,0,-1,-1, 0,-1, 1, 0,1 ]

def move_cnt(x,y,xp,yp):
    return math.sqrt( ((x - xp) **2 ) + ( (y - yp)**2 ))



# dx=[]
# dy = []