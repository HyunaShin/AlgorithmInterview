# -*- coding:utf8 -*-
from collections import deque
def bfs(graph, start, visited):
    '''
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
    2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고, 방문처리를 한다.
    3. 2번의 과정을 더이상 수행할 수 없을 떄 까지 반복한다.
    '''
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return

if __name__ == "__main__":
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]
    visited = [False] * 9
    bfs(graph, 1, visited)