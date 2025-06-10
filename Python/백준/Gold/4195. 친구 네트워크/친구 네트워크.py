import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        size[x_root] += size[y_root]

T = int(input())
for _ in range(T):
    f = int(input())
    idx = 0
    name_to_idx = dict()
    parent = dict()
    size = dict()
    for _ in range(f):
        a, b = input().split()
        for name in (a, b):
            if name not in name_to_idx:
                name_to_idx[name] = idx
                parent[idx] = idx
                size[idx] = 1
                idx += 1
        union(name_to_idx[a], name_to_idx[b])
        root = find(name_to_idx[a])
        print(size[root])