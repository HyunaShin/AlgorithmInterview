n,k = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

a.sort()
b.sort()

for _ in range(k):
    a[:k],b[-k:] = b[-k:], a[:k]

print(sum(a))