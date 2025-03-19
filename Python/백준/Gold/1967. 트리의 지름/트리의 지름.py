"""
가장 긴 경로 찾기
bfs 두 번
아무 노드에서 가장 먼 노드 찾고 그 노드에서 가장 먼 노드 찾으면 됨

"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    try:
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    except:
        break
# print(graph)
def bfs(start):
    q = deque([(start, 0)])
    visited = [False]*(n+1)
    visited[start] = True
    max_dis = 0
    max_node = 0
    
    while q:
        pos, dis = q.popleft()
        for g in graph[pos]:
            if not visited[g[0]]:
                q.append((g[0], dis+g[1]))
                visited[g[0]] = True
                if max_dis < dis+g[1]:
                    max_dis = dis+g[1]
                    max_node = g[0]
        # print(max_node, max_dis)
    return max_node, max_dis
node, val = bfs(1)

print(bfs(node)[1])



    


