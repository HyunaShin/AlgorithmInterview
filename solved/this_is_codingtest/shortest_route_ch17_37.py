import sys
input = sys.stdin.readline

n = int(input().rstrip())
#최대 10만개의 버스. O(N^3)까지는 설계 가능하다
m = int(input().rstrip())

#그래프 초기화
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

#그래프에 값 부여
for _ in range(m):
    a,b,c = map(int, input().rstrip().split(" "))
    #시작도시 -> 도착도시 의 cost
    #시작도시와 도착도시를 연결하는 노선은 하나가 아닐 수있다.
    graph[a][b] = min(c, graph[a][b])

# 자기자신에서 자기자신은 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

# 최솟값 구하기, 바로갔을떄 vs k를 경유했을떄
for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1,n+1):
        if graph[i][j] <  INF:
            print(graph[i][j], end=" ")
        else:
            print(0, end=" ")
    print()