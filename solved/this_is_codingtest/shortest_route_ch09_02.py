
def main():
    '''
    다익스트라로 풀었다!
    혀나쓰 넘 대단해~~~
    장하다 마이걸~~~
    '''
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

    return None

def solution():
    '''
    1 -> k, k -> M까지의 최단 경로이니
    모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 플로이드 워셜 알고리즘을 쓰자
    그래서 1-> k 의 최단경로 + k -> M까지의 최단 경로를 구해보자
    '''
    import sys
    INF = int(1e9)
    input = sys.stdin.readline
    n,m = map(int, input().rstrip().split(" "))
    graph = [[INF] * (n+1) for _ in range(n+1)]

    #자기 자신에게서 자기 자신으로 가는 비용은 0으로 초기화 하는 로직 까먹지 말것
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    for i in range(m):
        a,b = map(int, input().rstrip().split(" "))
        graph[a][b] = 1
        graph[b][a] = 1

    x,k =  map(int, input().rstrip().split(" "))

    for c in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

    result = graph[1][k] + graph[k][x]
    if result <= INF:
        print(result)
    else:
        print(-1)
    return

if __name__ == "__main__":
    solution()