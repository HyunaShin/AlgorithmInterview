def main():
    import sys
    import heapq
    input = sys.stdin.readline
    t = int(input().rstrip())
    INF = int(1e9)
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    for i in range(t):
        n = int(input().rstrip())
        #최단거리 테이블 초기화
        distance = [[INF] * n for _ in range(n)]
        #그래프에 값 넣기
        graph = [[] * n for _ in range(n)]
        for i in range(n):
            graph[i] = list(map(int, input().rstrip().split(" ")))
        q = []
        start = (0,0)
        heapq.heappush(q, (graph[0][0], start[0], start[1]))

        while q:
            dist_now, x, y = heapq.heappop(q)
            if distance[x][y] < dist_now:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx <n and 0 <= ny < n :
                    cost = dist_now + graph[nx][ny]
                    if distance[nx][ny] >  cost:
                        distance[nx][ny] = cost
                        heapq.heappush(q, (cost, nx, ny))

        print(distance[n-1][n-1])

    return

def solution():
    '''
    2차원의 다익스트라 알고리즘을 수행 하자.
    탐색은 좌표로 하고
    최단 거리도 좌표에 업데이트 한다.
    대신에 상하좌우 탐색은, 이동 가능한 노드를 파악할 때 하자
    '''
    import heapq
    import sys
    input = sys.stdin.readline
    INF = int(1e9)

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    for tc in range(int(input().rstrip())):
        n = int(input().rstrip())

        #전체 맵 정보를 입력 받기
        graph = []
        for i in range(n):
            graph.append(list(map(int, input().rstrip().split(" "))))

        #최단거리 테이블을 모두 무한으로 초기화
        distance = [[INF] * n for _ in range(n)]
        x,y =0,0 #시작 위치는 (0,0)

        #시작 노드로 가기 위한 비용은(0,0)위치의 값으로 설정하여, 큐에 삽입
        q = [(graph[x][y], x, y)]
        distance[x][y] = graph[x][y]

        #다익스트라 알고리즘 수행
        while q:
            #가장 최단거리가 짧은 노드에 대한 정보를 꺼내기
            dist, x, y = heapq.heappop(q)
            #현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[x][y] < dist:
                continue

            #현재 노드와 연결된 다른 인접한 노드를 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #맵의 경우를 벗어나는 경우 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
        print(distance[n-1][n-1])
    return

if __name__ == "__main__":
    main()