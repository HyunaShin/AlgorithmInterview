import sys

def find(root_tbl,x):
    if root_tbl[x] != x:
        return find(root_tbl, root_tbl[x])

    return root_tbl[x]

def union(root_tbl, a,b):
    ra = find(root_tbl, a)
    rb = find(root_tbl, b)
    if ra > rb:
        root_tbl[ra] = rb
    else:
        root_tbl[rb] = ra
    return root_tbl

input = sys.stdin.readline
n,m = map(int, input().rstrip().split())
#루트 테이블
root_tbl = [i for i in range(n+1)]
print(root_tbl)

for _ in range(m):
    cal,a,b = map(int,input().rstrip().split())
    if cal == 0:
        root_tbl = union(root_tbl, a,b)
    else:
        ra = find(root_tbl, a)
        rb = find(root_tbl, b)
        if ra == rb:
            print("YES")
        else:
            print("NO")
