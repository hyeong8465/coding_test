import heapq
import sys
input = sys.stdin.readline
inf = float('inf')

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

route = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    route[start].append(start)

    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for g in graph[now]:
            cost = dis + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))
                route[g[0]] = route[now]+[g[0]]
    return distance, route

dis, r = dijkstra(start)
print(dis[end])
print(len(r[end]))
print(*r[end])