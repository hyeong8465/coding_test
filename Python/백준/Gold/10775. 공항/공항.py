import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

g = int(input())
p = int(input())

# 유니온 파인드용 부모 테이블
parent = [i for i in range(g + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    parent[x_root] = y_root

answer = 0
for _ in range(p):
    gate = int(input())
    root = find(gate)
    if root == 0:
        break
    union(root, root - 1)
    answer += 1

print(answer)