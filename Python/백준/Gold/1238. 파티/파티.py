"""
09:30
단방향 간선

오고 가는데 가장 많은 시간을 소비하는 학생?

n: 1~1천
m: 1~1만

시간제한 1초:

플로이드 워셜: 10억 = 1000**3 -> 시간초과
모든 사람에 대해 다익스트라 2번

"""
import heapq as hq
import sys
input = sys.stdin.readline
inf = float('inf')

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    

def dijkstra(start, end):
    q = [(0, start)]
    distance = [inf]*(n+1)
    distance[start] = 0

    while q:
        dis, now = hq.heappop(q)
        if distance[now] < dis:
            continue
        
        for e, cost in graph[now]:
            c = dis+cost
            # print(e)
            if c < distance[e]:
                distance[e] = c
                hq.heappush(q, (c, e))
    # print(distance)
    return distance[end]

answer = 0
for i in range(1, n+1):
    res = dijkstra(i,x) + dijkstra(x,i)
    answer = max(res, answer)

print(answer)