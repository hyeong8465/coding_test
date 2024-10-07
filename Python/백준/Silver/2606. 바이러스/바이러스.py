import sys
from collections import deque

input = sys.stdin.readline

com = int(input())
n = int(input())
arr = [[] for _ in range(com+1)]
for i in range(1, n+1):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

visited = [False]*(com+1)
q = deque([1])
visited[1] = True
answer = 0
while q:
    # print(q)
    pos = q.popleft()
    for idx in arr[pos]:
        if visited[idx] == False:
            q.append(idx)
            visited[idx] = True
            answer += 1
print(answer)