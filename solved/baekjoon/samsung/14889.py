from itertools import permutations, combinations
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)] #O(N)
diff = int(1e9) #O(1)
players = [i for i in range(n)] #O(N)

for start in combinations(players, n//2): #O(N!)
    link = set(players) - set(start) #O(N//2)
    sp , lp = 0, 0 #O(2)
    for i in start: #O(n//2)
        for j in (set(start)-{i}): #O((n//2) - 1)
            sp +=  s[i][j]
    for i in link:
        for j in (link-{i}):
            lp += s[i][j]
    diff=min (diff, abs(sp -lp))
print(diff)