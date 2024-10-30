import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    a,b = map(int, input().rstrip().split())
    if a == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n+1)
    q = deque([(start, 0)])
    visited[start] = True
    while q:
        s, cnt = q.popleft()
        for i in graph[s]:
            if not visited[i]:
                q.append((i,cnt+1))
                visited[i] = True
    return cnt
answer = []
for j in range(1,n+1):
    answer.append([j,bfs(j)])
answer.sort(key = lambda x: x[1])

second = []
score = answer[0][1]
count = 0
for i in answer:
    if i[1] == score:
        count+=1
        second.append(i[0])

print(score, count)
print(*second)