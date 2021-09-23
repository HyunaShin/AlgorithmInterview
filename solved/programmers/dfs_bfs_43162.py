from collections import deque
import copy
def solution(n, computers):
    '''
    그래프 탐색을 통해 노드와 모든 연결된 노드를 탐색하고, 시작 노드를 방문처리
    computers모든 노드에 대해 반복한다.
    '''
    def dfs(graph, v, visited):
        visited[v] = True
        n = len(graph)
        for node in range(n):
            if graph[v][node] == 1 and visited[node] == False:
                dfs(graph, node, visited)

    answer = 0
    visited = [0] * n
    for start in range(n): #n개의 노드를 각각 시작노드로 dfs
        if visited[start] == 0: #이전 탐색에서 방문하지 않았을 경우에만 탐색 시작
            dfs(computers, start, visited)
            answer +=1
    return answer

def main(n, computers):
    result = dict()
    for s in range(n):  # N
        q = deque()  # 1
        q.append(s)  # 1
        visit_info = set()
        visit_info.add(s)
        tmp = copy.deepcopy(computers)
        while q:  # N
            c = q.popleft()  # 1
            for i in range(n):
                if tmp[c][i] ==1:
                   visit_info.add(i)
                   q.append(i)
                # if i == c:
                #     tmp[c][i] = 0
                # else:
                #     tmp[c][i] = 0
                #     tmp[c][i] = 0
            # for i in range(n):  # N
            #     if i == c:  # 1
            #         tmp[c][i] = 0  # 2n+1
            #         # visit_info.add(i)
            #     else:  # 1
            #         if tmp[c][i] == 1: #1
            #             tmp[c][i] = 0  # 2n+1
            #             tmp[i][c] = 0  # 2n+1
            #             q.append(i)  # 1
            #             # visit_info.add(i)


        result[s] = visit_info
    print(result)



# 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]] -> 2
# 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]] ->1
if __name__ == "__main__":
    ret = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]] )
    # ret = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(ret)