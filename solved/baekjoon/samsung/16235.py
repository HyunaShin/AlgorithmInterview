n,m,k = map(int, input().split())
tree_board =[[[] for _ in range(n)] for _ in range(n)]
land_board= [[5] * n for _ in range(n)]
energy_board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for _ in range(m):
    x,y,z = map(int, input().split())
    tree_board[x-1][y-1].append(z)


def spring_summer():
    for i in range(n):
        for j in range(n):
            trees = tree_board[i][j]
            if len(trees):
                trees.sort()
                temp_tree, dead_tree = [], 0
                for idx, tree in enumerate(trees):
                    if land_board[i][j] >= tree :
                        land_board[i][j] -= tree
                        tree+= 1
                        temp_tree.append(tree)
                    else:
                        #왜 곧바로 더하면 답이 다를까ㅜㅜ
                        dead_tree += tree//2
                        # land_board[i][j] += int(tree/2)
                land_board[i][j] += dead_tree
                tree_board[i][j] = []
                tree_board[i][j].extend(temp_tree)
    return

def fall():
    for x in range(n):
        for y in range(n):
            trees = tree_board[x][y]
            if len(trees):
                for tree in trees:
                    if tree%5 == 0:
                        for i in range(8):
                            nx = dx[i]+x
                            ny = dy[i] + y
                            if 0 <= nx < n and 0<= ny < n :
                                tree_board[nx][ny].append(1)

    return

def winter():
    for i in range(n):
        for j in range(n):
            land_board[i][j] += energy_board[i][j]
    return


for year in range(k):
    for season in range(3):
        if season ==0:
            spring_summer()
        elif season == 1:
            fall()
        else:
            winter()

tree_cnt = 0
for i in range(n):
    for j in range(n):
      tree_cnt += len(tree_board[i][j])
print(tree_cnt)

