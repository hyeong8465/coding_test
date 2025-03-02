import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # 도시의 수

if n == 1:
    print(0)
    quit()

m = int(input()) # 버스의 수

graph = [[] for _ in range(n+1)]

visited = [False]*(n+1)
distance = [INF]*(n+1)

for i in range(1, m+1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c)) # a->b 거리c

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

print(distance[end])






