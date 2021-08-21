# -*- coding:utf8 -*-

def dfs(graph, v, visited):
    '''
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    2. 스택의 최상단코드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문 처리를 한다.
        방문하지 않은 인접 노드가 없으면, 스택에서 최상단 노드를 꺼낸다.
    3. 2.번의 과정을 더이상 수행할 수 없을 때 까지 반복한다.
    '''
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i, visited)


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
    dfs(graph, 1, visited)