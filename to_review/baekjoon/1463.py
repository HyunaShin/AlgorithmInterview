# import copy
from collections import deque
n = int(input().strip())
#1로 만드는 최소 횟수만 넣는다
d = [0] * (n+1)

for i in range(2, n+1):
    #이전 횟수에서 1을 더한 값
    d[i] = d[i-1] +1
    #1을 더해주기 vs, 3으로 나눈 수의 최소 횟수
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    #1을 더해주기 vs 2로 나눈 수의 최소 횟수
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
print(d[i])
#     to_devide =i
#     q = deque([])
#     #모든 조건을 다 넣어바야함
#     q.append((i, i - 1, 1))
#     if i%3 == 0:
#         q.append((i, i/3,1))
#     if i %2 == 0:
#         q.append((i, i/2,1))
#
#     while q:
#         #나눌 수, 나눈 결과, 연산 횟수
#         to_devide, cal_result, num_cal = q.popleft()
#         #나눈 결과가 1이면, 최소 연산 횟수인지 확인하고 디피테이블에 넣음
#         #큐 소진
#         if cal_result == 1:
#             if dp_table.get(i):
#                 dp_table[i] = min(dp_table[i], num_cal)
#             else:
#                 dp_table[i] = num_cal
#         #아닌경우엔, 디피테이블에 있는지 보고
#         #지금까지 연산 횟수 + 이전의 최소 횟수를 큐에 넣어준다
#         elif dp_table.get(cal_result):
#             q.append((cal_result, 1,num_cal+dp_table.get(cal_result)))
#
#         #디피테이블에도 없다..? 새로 연산해주삼
#         else:
#             q.append((to_devide, to_devide-1, num_cal +1))
#             if i%3 == 0:
#                 q.append((to_devide, to_devide/3, num_cal+1))
#             if i%2 == 0:
#                 q.append((to_devide, to_devide/2, num_cal+1))
#
# print(dp_table[n])
