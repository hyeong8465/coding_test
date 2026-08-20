def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1

def solution(n, computers):
    parent = list(range(n))
    rank = [0]*n

    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                union(parent, rank, i, j)

    roots = {find(parent, i) for i in range(n)}
    return len(roots)