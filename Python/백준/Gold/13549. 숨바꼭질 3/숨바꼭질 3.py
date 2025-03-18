"""
최적화
"""
from collections import deque

n, k = map(int, input().split())

graph = [] # 0은 그냥 추가
for i in range(0, 100001):
    graph.append([2*i, i-1, i+1])
visited = [False]* 100001
visited[0] = True

q = deque([(n,0)])
if n > k:
    print(n-k)
    quit()

while q:
    # print(q)
    pos, sec = q.popleft()
    if pos == k:
        print(sec)
        quit()
    for i, g in enumerate(graph[pos]):
        if g >= 100001 or g <= -1:
            continue
        if not visited[g]:
            if i == 0:
                visited[g] = True
                q.appendleft((g, sec))
            else:
                visited[g] = True
                q.append((g, sec+1))