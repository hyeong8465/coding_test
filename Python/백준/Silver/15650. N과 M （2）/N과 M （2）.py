from itertools import combinations


n, m = map(int, input().split())
arr = [i for i in range(1,n+1)]
combi = list(combinations(arr, m))

for c in combi:
    print(*c)