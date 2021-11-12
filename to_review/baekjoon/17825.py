# https://www.acmicpc.net/problem/17825
#red는 0번째 인덱스
#blue는 1번째 인덱스
#dict로 풀자
# https://blog.encrypted.gg/732
def main():
    from collections import deque
    import copy
    dice = list(map(int, input().split()))
    e = {'s': [0],0 : [1], 1 : [2], 2 :[3], 3: [4], 4 : [5,9],
             5 : [6], 6 : [7], 7 : [8],
             9 : [10], 10 : [11], 11 : [12], 12 : [13],13 : [14, 16],
             14 : [15], 15 :[ 8],
             16: [17], 17: [18], 18: [19], 19: [20], 20 : [21, 24],
             21 : [22 ], 22 : [23], 23 : [8],
             24 : [25 ], 25 : [26], 26 : [27], 27 : [28],
             8 :[29 ], 29 : [30], 30 : [28], 28:['e']
             }
    v = [2, 4, 6, 8, 10,
                 13,16, 19,25,
                 12, 14, 16,18,20,
                 22, 24,
                 22, 24, 26,28,30,
                 28,27,26,
                 32, 34, 36, 38, 40,
                 30, 35,]

    vvvv ={'s' : ['a','b',"c",'d'], 'e' : []}
    hhhh ={'a':'s', 'b':'s', 'c':'s', 'd':'s'}

    def bfs(v_info, horse_info):
        q = deque()
        #말번호,칸번호, 주사위 인덱스, 위치별 말, 말별위치, score, rb
        q.append(('a','s', 0,v_info,horse_info, 0, 'r'))
        horse_info['a'] = v[dice[0]]
        v_info[v[dice[0]]]='a'
        max_score = 0
        while q:
            hidx, kan_idx, dice_idx, v_info,horse_info, score, rb = q.popleft()
            print(hidx, kan_idx, dice_idx, v_info,horse_info, score, rb)
            origin_kan = copy.deepcopy(kan_idx)
            #도착칸에 있지 않은 말을 골라야함.
            if (dice_idx > 10):
                print(score, "\n\n")
                max_score = max(max_score, score)
                break
            if  hidx in v_info.get('e'):
                continue

def solution():
    graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17],
             [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
    score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28,
             27, 26, 30, 35, 0]

    dice = list(map(int, input().split()))
    answer = 0
    def backtracking(loc, result, horse, test):
        global answer
        if loc > 10:
            answer = max(answer, result)
            return
        #말 네개에 대해서
        for i in range(4):
            x = horse[i]
            #말의 칸이 파란색에 있다면
            if len(graph[x]) == 2:
                #1번째 인덱스에 있는 칸
                x = graph[x][1]
            else:
                #아니면 0번째 인덱스에 있는 칸
                x = graph[x][0]

            #주사위를 던져서 칸을 이동한다.
            for j in range(1, dice[loc]):
                x = graph[x][0]
            if x == 32 or (x < 32 and x not in horse):
                #방문한적이 없거나, 다 탐색했으면
                #일단 이전값 카피 해 놓고
                before = horse[i]
                #말 이동 시키기
                horse[i] = x
                #test에 지금 위치 append
                test.append(x)
                #재귀적으로 호출
                backtracking(loc+1, result + score[x], horse, test)
                # test.pop()
                # #호출이 끝났으면 재귀적으로 호출한 값을 꺼내옴(백트래킹)
                # horse[i] =before


    backtracking(0,0,[0,0,0,0],[])
    print(answer)

if __name__ == "__main__":
    # solution()


    graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8],
             [9], [10], [11, 25], [12], [13], [14], [15],
             [16, 27], [17], [18], [19], [20], [32], [22],
             [23], [24], [30], [26], [24], [28], [29], [24], [31], [20],
             [32]]
    score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
    dice = list(map(int, input().split()))
    answer = 0
    def backtracking(loc, result, horse, test):
        global answer
        if loc >= 10:
            answer = max(answer, result)
            return

        for i in range(4):
            x = horse[i]
            if len(graph[x]) == 2:
                x = graph[x][1]
            else:
                x = graph[x][0]
            for j in range(1, dice[loc]):
                x = graph[x][0]
            if x == 32 or (x < 32 and x not in horse):
                before = horse[i]
                horse[i] = x
                # 지금 선택한 depth에 맞게 쭉 보냈다가
                backtracking(loc + 1, result+score[x],horse, test)
                #되돌아오게했음
                #이렇게 하면, 재귀적으로 1번~4번을 모두 다 한번씩 맨 마지막 선택지까지 보내 보게 됨.
                #누구를 먼저놓고 다음에 놓는게 베스트인지 찾을 수 있다.
                horse[i] = before

    backtracking(0, 0, [0,0,0,0], [])
    print(answer)
