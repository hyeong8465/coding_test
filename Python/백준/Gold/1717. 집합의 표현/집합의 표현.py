"""
15:30
0 a b -> a가 포함된 집합과 b가 포함된 집합을 합침
1 a b -> 두 원소 a, b가 같은 집합에 포함되어 있는지 확인 (yes/no)

n, 1백만
m, 10만
2초

try 1: 초기값 hash map에 저장, 두 집합이 병합되면 인덱스 숫자가 작은 쪽에 저장하고 큰 쪽엔 병합된 인덱스만 저장
-> 안될 것 같아서 유니온 파인드 공부



"""
import sys
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parents[y_root] = x_root

n, m = map(int, input().split())
parents = list(range(n+1))

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a,b)
    else:
        print('YES' if find(a) == find(b) else 'NO')