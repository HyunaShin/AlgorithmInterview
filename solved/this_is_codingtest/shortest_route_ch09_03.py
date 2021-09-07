import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n,m,c = map(int, input().rstrip().split(" "))
#노드별 최단거리
distance = [INF]*(n+1)
#노드로 이동하는 비용
array = [[] * n for _ in range(n+1)]

for _ in range(m):
    x,y,z = map(int, input().rstrip().split(" "))
    #array[노드] = (드는 비용, 이동할 노드)
    array[x].append((z,y))

#다익스트라
q = []
heapq.heappush(q, (0,c))
# !!!!distance초기화 조심
distance[c] = 0
while q:
    dist_now, node_now = heapq.heappop(q)
    # 원래 최단경로보다, 큐에서 가져온 최단 경로가 더 길면 무시한다.
    if distance[node_now] < dist_now:
        continue
    for dist_next, node_next in array[node_now]:
        #이동할 노드의 최단거리가, 지금 노드까지의 거리 + 이동할때의 거리보다 길면 최단경로 업데이트
        cost = dist_now + dist_next
        if distance[node_next] > cost:
            #최단경로 업데이트
            distance[node_next] = cost
            #여기서 다음 노드를 탐색
            heapq.heappush(q, (cost, node_next))


#이렇게 되면, 최단 경로 테이블은 c에서 출발했을 떄 최소값이게끔 업데이트가 된다.
#도시의 총 갯수는, 최단 경로 테이블이 INF가 아닌 경우만 찾으면 된다.
total_city = 0
total_cost = 0
print(distance)
for dist in distance:
    if dist < INF:
        total_city +=1
        total_cost = max(dist, total_cost)

print(total_city-1, " ", total_cost)