n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
roads = []

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(board[j][i])
    roads.append(board[i])
    roads.append(tmp)
from pprint import pprint
# pprint(roads)
# exit()
result = 0
for road in roads:
    print(road)
    slape = [False] * n
    flat_cnt = 0
    # 오른쪽이 더 높은 경우
    for i in range(0, n-1):
        print(road, i, i+1)
        #왼쪽보다 오른쪽이 한칸 높으면
        #길이가 l인 경사로를 둔다.
        if road[i+1] - road[i] == 1:
            #평평한 길이 경사로 길이보다 크거나 같으면(연속된 같은 칸의 높이)
            print(l, len(road[i-l:i]), [road[i] + 1] * l)
            if flat_cnt >= l:
                #경사로 놓는다
                road[i-l:i+1] = [road[i] + 1] * (l+1)
                slape[i - l:i + 1] = [True] * (l+1)
                # 다 놨으니까, 경사로 정보 초기화(다음 스텝에는 여기부터가 평평한구간)
                flat_cnt = 1
        #평평한 길이면(낮은 지점의 칸의 높이가 같으면)
        elif road[i+1] - road[i] == 0:
            #평평하다는 힌트 주기(연속이라는 정보)
            flat_cnt +=1

        #둘 사이 칸 차이가 1을 넘으면,평평한 길이 아니니까 초기화
        else:
            flat_cnt = 1
    print(road)
    print("-------")
    #왼쪽이 더 높은 경우
    flat_cnt = 0
    # 오른쪽이 더 높은 경우
    for i in range(n-1,0,-1):
        print(road, i-1, i)
        #오른보다 왼쪽이 한칸 높으면
        #길이가 l인 경사로를 둔다.
        if road[i-1] - road[i] == 1:
            #평평한 길이 경사로 길이보다 크거나 같으면(연속된 같은 칸의 높이)
            if flat_cnt >= l:
                #경사로 놓는다
                road[i:i+l] = [road[i] + 1] * l
                slape[i:i+l] = [True] * (l)
                # 다 놨으니까, 경사로 정보 초기화(다음 스텝에는 여기부터가 평평한구간)
                flat_cnt = 1
        #평평한 길이면(낮은 지점의 칸의 높이가 같으면)
        elif road[i] - road[i-1] == 0:
            #평평하다는 힌트 주기(연속이라는 정보)
            flat_cnt +=1

        #둘 사이 칸 차이가 1을 넘으면,평평한 길이 아니니까 초기화
        else:
            flat_cnt = 1

    #갈수 있는 길인지 체크
    if len(set(road)) == 1:
        result +=1
        slape = [True] * n
    print(road)
    print(slape)
    print("=======")

print(result)