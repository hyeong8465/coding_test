"""
13:43
1. 다익스트라로 시작점마다 최단 경로 만들고 범위에 들어오는 아이템 합산 후 업데이트
2. 플로이드로 미리 최단 경로 테이블 만들어?

"""
import heapq
import sys
input = sys.stdin.readline
inf = float('inf')

# 입력
n, m ,r = map(int, input().split()) # 지역, 수색범위, 간선
items = list(map(int, input().split()))

# 그래프
graph = [[] for _ in range(n+1)]
for _ in range(r):
    i,j,k = map(int, input().split())
    graph[i].append((k, j))
    graph[j].append((k, i))

def dijkstra(start):
    distance = [inf] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for g in graph[now]:
            cost = dist+g[0]
            if cost < distance[g[1]]:
                heapq.heappush(q, (cost, g[1]))
                distance[g[1]] = cost
    return distance

ans = 0
for i in range(1, n+1):
    dis = dijkstra(i)
    temp = 0
    for j in range(1, len(dis)):
        if dis[j] <= m:
            temp += items[j-1]
    ans = max(ans, temp)
print(ans)







