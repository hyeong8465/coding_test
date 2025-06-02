import heapq
import sys
input = sys.stdin.readline

n, d = map(int, input().split())
edges = [[] for _ in range(d + 1)]

# 일반 도로: i -> i+1 간선 추가 (비용 1)
for i in range(d):
    edges[i].append((i + 1, 1))

# 지름길 정보 추가
for _ in range(n):
    a, b, c = map(int, input().split())
    if b <= d:  # b가 도착 지점 d를 넘어가면 무시
        edges[a].append((b, c))

# 다익스트라
INF = float('inf')
dist = [INF] * (d + 1)
dist[0] = 0
pq = [(0, 0)]  # (거리, 노드)

while pq:
    cost, node = heapq.heappop(pq)
    if dist[node] < cost:
        continue
    for next_node, weight in edges[node]:
        if dist[next_node] > cost + weight:
            dist[next_node] = cost + weight
            heapq.heappush(pq, (dist[next_node], next_node))

print(dist[d])