from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
c_list = list(map(int, input().split()))
dp_table = dict()
max_val, min_val = -1000000000, 1000000000
# 연산자 : 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
#(연산자, 연산자 인덱스) 로 만듬
c_cases = []
for c, c_idxes in enumerate(c_list): #O(11 * 10)
    for c_idx in range(c_idxes):
        c_cases.append((c, c_idx))

#조합을 만들고 하나씩 가져오면서
for calcultation in permutations(c_cases):#O(10! * 40)
    #연산자만 빼온다
    order = []
    for c in calcultation: #O(10)
        order.append(c[0])
    order = tuple(order)
    #똑같은 연산을 한번 했으면 패스
    if dp_table.get(order) ==None: #O(23)
        #시드로 넘기는 번호
        local_sum = numbers[0]
        idx = 1
        for c in order: #O(10 + 8)
            if c == 0: #O(4)
                local_sum += numbers[idx]
                idx +=1
            elif c == 1:
                local_sum -= numbers[idx]
                idx +=1

            elif c == 2:
                local_sum *= numbers[idx]
                idx +=1

            else: #O(8)
                if local_sum < 0:
                    local_sum = ((local_sum * -1)//numbers[idx]) * -1
                    idx +=1
                else:
                    local_sum = local_sum//numbers[idx]
                    idx +=1

        dp_table[order] = True
        max_val = max(max_val, local_sum)
        min_val = min(min_val, local_sum)
#O(10! * 40) + O(11 * 10)
print(max_val)
print(min_val)
# 137656	1888