n = int(input())
board= [list(map(int, input().split())) for _ in range(n)]
election_board = [[0] * (n+1) for _ in range(n+1)]


def get_boundary(election_board, x,y,d1,d2):
    d1_list = [i for i in range(d1+1)]
    d2_list = [i for i in range(d2+1)]

    if n >= x+d1+d2  >= 0 and n >= y-d1+d2 >= 0 and\
            n>= x + d2+d1>= 0 and  n>= y +d2-d1>= 0 and \
            n >= x + d1 >= 0 and n >= y-d1 >= 0 and \
            n >= x + d2 >= 0 and n >= y+d2 >= 0:
        #3번
        for j in d2_list:
            election_board[x+d1+j][y-d1+j] = 5
            # trial = 0
            # for i in range(n,x+d1-1,-1):
            #     for k in range(1, y-d1+j-trial+1):
            #         if election_board[i][k]==0:
            #         election_board[i][k] = 3
            #     trial +=1

        #4번
        for j in d1_list:
            election_board[x + d2+j][y +d2-j] =5
            # trial = 0
            # for i in range(n,x+d2, -1):
            #     for k in range(y-j+d2+trial,n+1):
            #         if election_board[i][k] == 0:
            #         election_board[i][k]= 4
            #     trial +=1

        #1번
        for d1 in d1_list:
            election_board[x+d1][y-d1] =5
            for i in range(1,x+d1):
                for j in range(1,y-d1+1):
                    # if election_board[i][j] == 0:
                    election_board[i][j]=1

        #2번
        for d2 in d2_list:
            election_board[x+d2][y+d2] =5
            trial = 0
            for i in range(1,x+d2+1):
                for j in range(y+trial, n+1):
                    # if election_board[i][j] == 0:
                    election_board[i][j]=2
                trial +=1
        #

        return election_board
    else:
        return None


from pprint import pprint
min_diff= int(1e9)
for x in range(1,n-2):
    for y in range(1,n-1):
        for d1 in range(1,n-x+1 ):
            for d2 in range(1, n-y+1):
                # if x == 2 and y == 4 and d1 == 2 and d2 == 2:
                # print(x,y,d1,d2)
                if x == 2 and y == 4 and d1 == 2 and d2 == 2:
                    nb = get_boundary(election_board, x, y, d1, d2)
                    if nb:
                        pprint(nb)



                # print(x,y)

# print(n-3, n-1, n-2, n-3)
# for d1 in range(1, n-3):
#     for d2 in range(1, n-2):
#         for x in range(1, n-1):
#             for y in range(1, n-2):
#                 # print(d1,d2,x,y)
#                 board = get_boundary(board, x,y,d1,d2)
#                 # if diff_cnt_list != None:
#                 # _max, _min = max(diff_cnt_list), min(diff_cnt_list)
#                 # min_diff = min(min_diff, _max - _min)
#                 if x == 3 and y == 3 and d1 == 1 and d2 ==1 :
#                     print(board)
#                     # if min_diff == _max - _min:
#                     #     print(min_diff)
#                     #     pprint(debug)

print(min_diff)
