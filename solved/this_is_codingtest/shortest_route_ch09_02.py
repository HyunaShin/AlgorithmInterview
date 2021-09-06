
import sys
import heapq
input = sys.stdin.readline
n,m = list(map(int, input().rstrip().split(" ")))
INF = int(1e9)
g = [[] * (n+1) for _ in range(n+1)]
start = 1

for i in range(m):
    _from, _to = list(map(int, input().rstrip().split(" ")))
    g[_from].append((1,_to))
    g[_to].append((1, _from))

dist = [INF] * (n + 1)
x,k = list(map(int, input().rstrip().split(" ")))
# print(g)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start]=0

    while q:
        cost, node = heapq.heappop(q)
        # print(cost,node)
        if cost > dist[node]:
            continue

        for linked_node_cost ,linked_node in g[node]:
            new_dist = cost + linked_node_cost
            if dist[linked_node] > new_dist:
                dist[linked_node] = new_dist
                heapq.heappush(q, (new_dist, linked_node))

    return dist

dijkstra(start)
dist_k = dijkstra(start)
route_k = dist[k]

dist_x = dijkstra(k)
route_x  = dist_x[x]


if route_x + route_k >= INF:
    print(-1)
else:
    print(route_x + route_k)
