def main():
    import copy
    n,m = map(int, input().split())
    targets = list(map(int, input().split()))
    q = [i for i in range(1, n+1)] #공간 복잡도 N
    total_cnt = 0

    for target in targets: #M
        left_cnt = 0 #1
        right_cnt = 0 #1
        #(N+1) * (3N+3)
        tmp = copy.deepcopy(q) #N, 공간 복잡도 N
        #왼쪽으로 밀어보기
        while target != tmp[0]: #N +1
            tmp = tmp[1:] + [tmp[0]] #3N +2
            left_cnt +=1 #1

        #오른쪽으로 밀어보기
        tmp = copy.deepcopy(q) #N
        while target != tmp[0]:  # N +1
            tmp =  [tmp[-1]] + tmp[:-1]  # 3N +2
            right_cnt += 1 #1

        #밀어봤더니 더 적게 움직이면
        if left_cnt < right_cnt: #1
            # 왼쪽으로 밀어보기
            while target != q[0]:  # N +1
                q = q[1:] + [q[0]]  # 3N +1
                total_cnt +=1 #N

        else: #1
            while target != q[0]:  # N +1
                q = [q[-1]] + q[:-1]  # 3N +1
                total_cnt +=1 #N
        q.pop(0) #N

    print(total_cnt)

def solution():
    '''
    왼쪽으로 슬라이딩 할 경우, 오른쪽으로 할 경우 몇번 가야하는지 미리 보고, 더 빠른 쪽으로 한번에
    '''
    n, m = map(int, input().split())

    position = list(map(int, input().split()))

    que = list(range(1, n + 1))

    count = 0
    for i in range(len(position)):
        left = len(que) - que.index(position[i])
        right = que.index(position[i])

        if right != 0:
            if left < right:
                for _ in range(left):
                    que.insert(0, que[-1])
                    del que[-1]
                count = count + left
            else:
                for _ in range(right):
                    que.append(que[0])
                    del que[0]
                count = count + right

        del que[0]

    print(count)