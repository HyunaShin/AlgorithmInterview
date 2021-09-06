# import sys
#
# _a = sys.stdin.readline().rstrip()
# _b = sys.stdin.readline().rstrip()
#
# a = dict()
# b = dict()
# for idx, i in enumerate(_a):
#     a[idx] = i
#
# for idx, i in enumerate(_b):
#     b[idx] = i
#
# cnt = 0
# for i in range(len(a.keys())):
#     for j in range(len(b.keys())):
#         if a[i] == b[i]:
#             continue
#         elif a[i] == b[j]:
#             replaced = j-i
#

def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    #dp테이블 초기 설정
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    #최소 편집 거리 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            #문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            #문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            #삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
            else:
                dp[i][j] = 1+min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[n][m]

str1 = input()
str2 = input()
print(edit_dist(str1, str2))