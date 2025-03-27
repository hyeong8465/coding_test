from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# print(graph)

def bfs(start):
    visited = [False]*(n+1)
    q = deque([[start,0]])
    visited[start] = True
    answer = []

    while q:
        p,d = q.popleft()
        if d == k:
            answer.append(p)
        for g in graph[p]:
            if not visited[g]:
                q.append([g,d+1])
                visited[g] = True
    return answer

answer = bfs(x)
if len(answer) == 0:
    print(-1)
else:
    answer = sorted(answer)
    for a in answer:
        print(a)