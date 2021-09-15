def main():
    import sys
    def find(root_tbl, x):
        if x != root_tbl[x]:
            return find(root_tbl,root_tbl[x])
        return root_tbl[x]

    def union(a,b):
        ra = find(root_tbl, a)
        rb = find(root_tbl, b)
        if ra > rb:
            root_tbl[ra] = rb
        else:
            root_tbl[rb] = ra

    input = sys.stdin.readline
    n,m = map(int, input().rstrip().split())
    root_tbl = [i for i in range(n+1)]

    edges = []
    result = 0

    for _ in range(m):
        a,b,c = map(int, input().rstrip().split())
        edges.append((c,a,b))

    edges.sort()
    final = 0
    for edge in edges:
        c,a,b = edge
        #루트는 find함수를 써서 찾을 수 있다. 기억 해 두자
        if find(root_tbl,a) != find(root_tbl,b):
            union(a,b)
            result += c
            final = c
    print(result - final)

def solution():
    '''
    문제의 핵심 아이디어는, 전체 그래프에서 2개의 최소 신장 트리를 만들어야 한다.
    --> 크루스칼 알고리즘으로 최소 신장 트리를 찾아 내고, 가장 비용이 큰 간선을 제거하자
    '''
    #특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        #루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    #두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    #노드의 개수와 간선의 개수 입력 받기
    v, e = map(int, input().split())
    #부모 테이블 초기화
    parent = [0] *(v+1)

    #모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges = []
    result = 0

    #부모 테이블에서, 부모를 자기 자신으로 초기화
    for i in range(v+1):
        parent[i] = i

    for _ in range(e):
        a,b,cost = map(int, input().split())
        edges.append((cost, a, b))

    #간선을 비용순으로 정렬
    edges.sort()
    last = 0 #최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선

    #간선을 하나씩 확인하며
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost
            last = cost
    print(result - last)

if __name__ == "__main__":
    # solution()
    main()