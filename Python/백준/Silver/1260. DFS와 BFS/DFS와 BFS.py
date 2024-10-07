import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
# print(arr)
for _ in range(m):
    s, e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)
for a in arr:
    a.sort()
# print(arr)

def bfs(v):
    answer = []
    visited = [False]*(n+1)
    q = deque([v])
    answer.append(v)
    visited[v] = True
    while q:
        s = q.popleft()
        for i in arr[s]:
            if visited[i] == False:
                q.append(i)
                answer.append(i)
                visited[i] = True
    print(*answer)
    return(answer)

visited = [False]*(n+1)
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in arr[v]:
        if not visited[i]:
            dfs(i)


dfs(v)
print('')
bfs(v)