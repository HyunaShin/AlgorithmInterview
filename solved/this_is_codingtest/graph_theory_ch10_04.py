def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    n= int(input().rstrip())

    coefficients = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    costs=[0] *(n+1)
    total_cost = 0

    q = deque()
    for i in range(1,n+1):
        node_info = list(map(int, input().rstrip().split()))[:-1]
        costs[i] = node_info[0]
        for linked_node in node_info[1:]:
            graph[i].append(linked_node)
            coefficients[linked_node] +=1


        #위상정렬알고리즘 수행
        #차수가 0인 노드를 찾아서 큐에 넣는다
        for j in range(1,n+1):
            if coefficients[j] == 0:
                #노드, 차수
                q.append(j)
                total_cost += costs[j]
        print(graph)
        print(costs)
        print(q)
        while q:
            s_node = q.popleft()
            print(s_node)
            for l_node  in graph[s_node]:
                # print(l_node)
                coefficients[l_node] -=1
                total_cost += costs[l_node]

            for j in range(1, n + 1):
                if coefficients[j] == 0:
                    # 노드, 차수
                    q.append(j)
            # for j in range(1, n + 1):
            #     if graph[j] != [] and coefficients[j] == 0:
            #         # 노드, 차수
            #         q.append(j)
        # print(total_cost)
    return None

def solution():
    from collections import deque
    import copy
    #노드의 개수 입력 받기
    v = int(input())
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (v+1)
    #각 노드에 연결된 간선 정보를 담기 위한 연결리스트(그래프)초기화
    graph = [[] for i in range(v+1)]
    #각 강의시간을 0으로 초기화
    time = [0] * (v+1)
    #방향 그래프의 모든 간선 정보를 입력받기
    for i in range(1, v+1):
        data = list(map(int, input().split()))
        time[i] = data[0] #첫번째 수는 시간 정보를 담고 있음
        for x in data[1:-1]:
            indegree[i] +=1
            graph[x].append(i)
    #위상 정렬 함수
    def topology_sort():
        #알고리즘 수행 결과를 담을 리스트
        result = copy.deepcopy(time)
        q = deque()
        #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, v+1):
            if indegree[i] == 0:
                q.append(i)
        #큐가 빌 때 까지 반복
        while q:
            #큐에서 원소 꺼내기
            now = q.popleft()
            #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                result[i] = max(result[i], result[now] + time[i])
                indegree[i] -=1
                #새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

        #위상정렬을 수행한 결과 출력
        for i in range(1, v+1):
            print(result[i])
    topology_sort()
    return

if __name__ == "__main__":
    solution()