"""
12:12

1번 노드에서 가장 멀리 떨어진 노드의 갯수

n = 2만
e = 5만
- bfs -> O(N+E)
- 다익스트라
- 플로이드 워셜


"""
from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    visited = [False]*(n+1)
    q = deque([(1,0)])
    visited[1] = True

    answer = 0
    max_dist = 0

    while q:
        start, dist = q.popleft()
        ndist = dist+1
        for end in graph[start]:
            if not visited[end]:
                q.append((end, ndist))
                visited[end] = True
                if max_dist < ndist:
                    max_dist = ndist
                    answer = 1
                elif max_dist == ndist:
                    answer += 1

    print(answer)
    return answer