from itertools import permutations

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for c in range(0,n):
    for a in range(0, n):
        for b in range(0, n):
            graph[a][b] = min(graph[a][b], graph[a][c]+graph[c][b])

ans = float('inf')
for per in permutations(range(n), n-1):
    if k not in per:
        temp = 0
        s = k
        for e in per:
            # print(p)
            temp += graph[s][e]
            s = e
        ans = min(ans, temp)
        # print(per)
print(ans)