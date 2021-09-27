a,b,c,d = [list(map(int, str(input()))) for _ in range(4)]
k = int(input())
directions = [list(map(int, input().split())) for _ in range(k)]
topni = {1 : a, 2: b, 3:c, 4:d}
s,r,l = 0,2,6

def check(a,b):
    if topni[a][r] != topni[b][l]:
        return True
    else:
        return False

def move(num ,d, check_info, trial):
    if check_info == False or trial[num] == True:
        return

    trial[num]=True
    if 1 < num < 4:
        move(num-1, d * -1 , check(num-1,num), trial)
        move(num + 1, d * -1,  check(num, num+1), trial)
    elif num == 1:
        move(num + 1, d * -1, check(num, num+1), trial)
    else:
        move(num-1, d * -1, check(num-1, num), trial)

    tmp = [0] * 8
    for i in range(8):
        tmp[(i + (1 * d)) % 8] = topni[num][i]
    topni[num] = tmp

for t,dir in directions:
    trial = [0] * 5
    ret = move(t,dir,True, trial)

result = 0
for i in range(1, 5):
    result += (topni[i][0] *(2**(i-1)))
print(result)