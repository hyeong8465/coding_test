import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
arr = []
start = []
visited = [[False]*m for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

for r in range(n):
    for c in range(m):
        if arr[r][c] == 1:
            start.append((r,c,0))
            visited[r][c] = True
        elif arr[r][c] == -1:
            visited[r][c] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque(start)

while q:
    r, c, day = q.popleft()
    for i in range(4):
        pr, pc = r+dx[i], c+dy[i]
        if pr <= -1 or pr >= n or pc <= -1 or pc >= m:
            continue
        if arr[pr][pc] != -1 and visited[pr][pc] == False:
            q.append((pr, pc, day+1))
            visited[pr][pc] = True
            # print(q)
sum_val = 0
for v in visited:
    sum_val += sum(v)
if sum_val != n*m:
    print(-1)
else:
    print(day)