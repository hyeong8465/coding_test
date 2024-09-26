"""
걷 => x-1 or x+1
순 -> 2*x
모든 경우 그래프 표현
1: 2, 2
2: 1,2,4
3: 2,3,6
...


"""
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

graph = [] # 0은 그냥 추가
for i in range(0, 100001):
    graph.append([i-1, i+1, 2*i])
visited = [False]* len(graph)

q = deque([(n, 0)])

visited[n] = True
while q:
    x, cnt = q.popleft()
    if x == k:
        print(cnt)
        quit()
    for v in graph[x]:
        # print(graph[x])
        if v >= 100001 or v <= -1:
            continue
        if visited[v] == False:
            q.append((v, cnt+1))
            visited[v] = True