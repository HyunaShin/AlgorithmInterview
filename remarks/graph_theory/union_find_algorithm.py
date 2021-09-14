# 서로소 집합 알고리즘

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 떄 까지 재귀적으로 호출
    # https://rok93.tistory.com/entry/9-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%9D%B4%EB%A1%A0-%EC%84%9C%EB%A1%9C%EC%86%8C-%EC%A7%91%ED%95%A9
    # print(parent, x)
    if parent[x] != x:
        return find_parent(parent, parent[x])
    #재귀적으로 부모를 찾는 법
    # return x
    #find함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법
    # parent를 찾아낸 루트로 아예 바꿔버리면
    # Find 연산 수행시 중복되는 연산을 줄여준다.
    # (바로 다음번 동일한 find연산 수행시, 경로를 따라갈 ㅍㄹ요 없이 바로 루트를 찾을 수 있게된다.)
    # 재귀적인 구현 덕분에 u에서 루트까지 올라가는 경로 상에 있는
    # 모든 노드들에게도 경로 압축 최적화가 자동으로 수행된다.
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a,b):
    '''
    :param parent: 부모테이블
    :param a: 원소 a
    :param b: 원소 b
    부모 테이블에서 원소 a,b의 부모를 찾고 더 부모가 작은 쪽 원소의 부모를 가리키게끔.
    '''
    a = find_parent(parent, a)
    # print("========")
    b = find_parent(parent, b)
    # print("========")
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

#부모 테이블상에서, 부모를 자기자신으로 초기화 --> 원소(노드) 정보
for i in range(1, v+1):
    parent[i] = i

#union 연산을 각각 수행 --> 간선 정보
#간선 정보를 받아 오면서, 건바이건으로
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)
    # print(parent)

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end = "")
for i in range(1, v+1):
    print(find_parent(parent, i), end = " ")

print()
for i in range(1, v+1):
    print(parent[i], end=" ")