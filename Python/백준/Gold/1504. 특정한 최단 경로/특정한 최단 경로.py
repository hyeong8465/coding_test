"""
방향성 없음
최단 경로
조건 1. 임의로 주어진 두 정점은 반드시 통과
조건 2. 한번 이동한 정점과 간선 모두 이동 가능

단순히
1 -> 경유1 -> 경유2 -> n
1 -> 경유2 -> 경유1 -> n
의 최솟값을 출력하려고 했는데
이 경우 경유1에서 이미 경유2를 지난 경우를 고려하지 못함


"""
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = 1e9

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

a, b = map(int, input().split())

def dijkstra(s, e):
    distance = [INF] * (n+1)
    
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    if distance[e] == INF:
        return -1
    else:
        return distance[e]
ans1 = dijkstra(1, a)
ans2 = dijkstra(1, b)

if ans1 == -1 or ans2 == -1:
    print(-1)
    exit()

path1 = dijkstra(a, b)
path2 = dijkstra(b, n)
path3 = dijkstra(a, n)

if path1 == -1 or path2 == -1 or path3 == -1:
    print(-1)
else:
    print(min(ans1 + path1 + path2, ans2 + path1 + path3))