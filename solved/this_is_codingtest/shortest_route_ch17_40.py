import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
n,m = map(int, input().rstrip().split(" "))
#최단거리 테이블 초기화
distance = [INF] * (n +1)

#그래프 정보 받아오기(양방향 고려)
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().rstrip().split(" "))
    graph[x].append((1,y))
    graph[y].append((1,x))

q = []
#1번노드에서 출발하고, 출발은 비용이 들지 않는다.
heapq.heappush(q, (0,1))
distance[1] = 0

while q:
    dist, node = heapq.heappop(q)
    if dist > distance[node]:
        continue
    for n_dist, n_node in graph[node]:
        cost = n_dist + dist
        if cost < distance[n_node]:
            distance[n_node] = cost
            heapq.heappush(q, (n_dist,n_node))

max_dist = max(list(filter(lambda x : x != INF,distance)))
print( distance.index(max_dist), " ", max_dist, " ",distance.count(max_dist))

#---solution 중
max_node = 0
max_distance = 0
result = []
for i in range(1, n+1):
    #최댓값 찾고
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node ]
    #이후에 등장하는 값은 append
    elif max_distance == distance[i]:
        result.append(i)