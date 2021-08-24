# -*- coding:utf8 -*-
from collections import deque
def main(x):
    queue = deque()
    queue.append(x)
    visited[x] +=1

    while queue:
        _from = queue.popleft()
        for _to in graph[_from]:
            if visited[_to] == -1:
                #방문 안했으면이라는 조건때문에, 이미 방문한 노드는 안감 --> 최소 방문 수가 나올 수 있음
                visited[_to] = visited[_from] + 1
                queue.append(_to)

    return visited

def solution():
    n,m, k,x = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)

    distance = [-1] * (n+1)
    distance[x] = 0

    q = deque([x])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            print(now, distance, next_node, q)
            if distance[next_node] == -1:
                #다음 노드 = 지금 노드까지 비용 +1
                distance[next_node] = distance[now] +1
                q.append(next_node)


    check = False
    for i in range(1,n+1):
        if distance[i] == k:
            print(i)
            check = True

    if check == False:
        print(-1)

if __name__ == "__main__":
    n, m, k, x  = list(map(int, input().split(" ")))

    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    for i in range(m):
        a,b = list(map(int, input().split(" ")))
        graph[a].append(b)

    main(x)

    res = 0
    for idx, val in enumerate(visited):
        if idx == 0:
            continue
        elif val == k:
            res +=1
            print(idx)

    if res == 0:
        print(-1)
