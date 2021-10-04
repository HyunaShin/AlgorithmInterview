

def solution():
    from collections import Counter
    r,c,k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(3)]

    def R():
        copy_a = []
        max_len =0
        for tmp in A:
            tmp = Counter(tmp)
            # print(tmp)
            del (tmp[0])
            copy_tmp = sorted(tmp.items(), key = lambda x : (x[1], x[0]))
            tt = []
            for a in copy_tmp:
                tt.extend(a)
                if len(tt) == 100:
                    break
            max_len = max(max_len, len(tt))
            copy_a.append(tt)
        for ss in copy_a:
            ss += [0] * (max_len - len(ss))
        return copy_a

    time = 0
    while True:
        if time > 100:
            break
        if r <= len(A) and c<= len(A[0]) and A[r-1][c-1] ==k:
            break
        if len(A) >= len(A[0]):
            A = R()
        else:
            #How to transpose : A를 열별로 묶고 풀어주기
            A = list(map(list, zip(*A)))
            A = R()
            A = list(map(list, zip(*A)))
        time +=1
    if time > 100:
        print(-1)
    else:
        print(time)


def sort(set_arr, cnt_arr):
    if len(cnt_arr) <= 1:
        return set_arr, cnt_arr
    pivot=0
    front_set, front_cnt = [],[]
    back_set, back_cnt = [], []
    for i in range(pivot+1, len(cnt_arr)):
        if cnt_arr[pivot] < cnt_arr[i]:
            back_cnt.append(cnt_arr[i])
            back_set.append(set_arr[i])
        elif cnt_arr[pivot] > cnt_arr[i]:
            front_cnt.append(cnt_arr[i])
            front_set.append(set_arr[i])
        else:
            if set_arr[pivot] > set_arr[i]:
                front_cnt.append(cnt_arr[i])
                front_set.append(set_arr[i])
            else:
                back_cnt.append(cnt_arr[i])
                back_set.append(set_arr[i])

    fs, fc = sort(front_set, front_cnt)
    bs, bc = sort(back_set, back_cnt)
    return fs +[set_arr[pivot]] + bs, fc + [cnt_arr[pivot]] + bc

if __name__ == "__main__":
    r,c,k = map(int, input().split())
    a=[list(map(int, input().split())) for _ in range(3)]
    result = 0
    x_len, y_len = 3, 3
    while True:
        if result > 100:
            print(-1)
            break
        try:
            arc = a[r - 1][c - 1]
            if arc == k:
                print(result)
                break
        except IndexError as e:
            arc = int(1e9)

        if x_len >= y_len:
            return_mat = [[0] * 100 for _ in range(100)]
            for i in range(x_len):
                set_arr = []
                cnt_arr = []
                for j in sorted(set(a[i])):
                    if j != 0:
                        set_arr.append(j)
                        cnt_arr.append(a[i].count(j))
                set_arr, cnt_arr = sort(set_arr, cnt_arr)
                for idx, values in enumerate(zip(set_arr, cnt_arr)):
                    try:
                        # 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
                        return_mat[i][idx * 2], return_mat[i][(idx * 2) + 1] = values[0], values[1]
                    except IndexError as e:
                        break
                # 가로 길이만 늘어남
                y_len = max(y_len, len(cnt_arr) * 2)
            a = return_mat
            # print(a)
        #R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
        else:
            return_mat = [[0] * 100 for _ in range(100)]
            for j in range(y_len): #O(N**2)
                tmp = []
                for i in range(x_len):
                    if a[i][j] !=0:
                        tmp.append(a[i][j])

                set_arr = []
                cnt_arr = []
                for i in sorted(set(tmp)): #O(N)
                    set_arr.append(i)
                    cnt_arr.append(tmp.count(i)) #O(N)
                set_arr, cnt_arr = sort(set_arr, cnt_arr)#O(2NlogN)
                for idx, values in enumerate(zip(set_arr, cnt_arr)):
                    try:
                        return_mat[idx * 2][j], return_mat[(idx * 2) + 1][j] = values[0], values[1]
                    except IndexError as e:
                        break
                #세로길이만 늘어남
                x_len = max(x_len, len(set_arr)*2)
            a = return_mat
        result +=1