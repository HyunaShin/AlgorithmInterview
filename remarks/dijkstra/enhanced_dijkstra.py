import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

#노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().rstrip().split())
#시작 노드 번호를 입력 받기
start = int(input())

#각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
#최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력 받기
for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    #큐가 비어있지 않다면
    while q:
        #가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            #연결된 노드의 최소 비용 = 지금 최단거리 + 지금 그래프랑 연결된 노드로의 비용
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            #연결된 노드로 가는 최단거리가, 해당 노드의 원래 최단거리보다 짧다면
            if cost < distance[i[0]]:
                #해당 노드의 최단 거리를 업데이트한다.
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])