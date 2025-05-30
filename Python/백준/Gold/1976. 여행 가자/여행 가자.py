import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root

parent = list(range(n))
for i in range(n):
    conn = list(map(int, input().split()))
    for j in range(n):
        if conn[j] == 1:
            union(i,j)

plan = list(map(int, input().split()))
root = find(plan[0]-1)
for c in plan[1:]:
    if find(c-1) != root:
        print('NO')
        break
else:
    print('YES')