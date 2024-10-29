import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

def bfs(s):
    visited = [False]*(n+1)
    q = deque([(s,0)])
    visited[s] = True
    temp = []
    while q:
        start,cnt = q.popleft()
        for i in graph[start]:
            if not visited[i]:
                q.append((i,cnt+1))
                # print(q)
                temp.append(cnt+1)
                # print(s, temp)
                visited[i] = True
    # print(temp)
    return sum(temp)
answer = 10000000000
ans = 1
for p in range(1,n+1):
    val = bfs(p)
    # print(val)
    if val < answer:
        answer = val
        ans = p
print(ans)



    
