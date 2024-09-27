import sys
from collections import deque
input = sys.stdin.readline

node, line = map(int,input().split())
arr = [[] for _ in range(node+1)]
for a in range(line):
    s, e = map(int, input().rstrip().split())
    arr[s].append(e)
    arr[e].append(s)


visited = [False] * (node+1)
cnt = 0
for i in range(1, node+1):
    q = deque([i])
    # print(visited)
    if visited[i] == False:
        cnt += 1
    visited[i] = True
    while q:
        idx = q.popleft()
        for j in arr[idx]:
            if visited[j] == False:
                q.append(j)
                visited[j] = True
print(cnt)