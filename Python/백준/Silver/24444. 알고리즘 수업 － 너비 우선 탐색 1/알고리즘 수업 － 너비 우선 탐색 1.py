import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, graph, start):
    visited = [0] * (n + 1)
    q = deque([start])
    visited[start] = 1
    order = 1

    while q:
        v = q.popleft()
        for e in graph[v]:
            if visited[e] == 0:
                q.append(e)
                order += 1
                visited[e] = order

    return visited

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프이므로 양방향으로 추가

for i in range(1, n+1):
    graph[i].sort()  # 인접 정점을 오름차순으로 정렬

result = bfs(n, graph, r)

for i in range(1, n+1):
    print(result[i])