import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

def bfs(graph):
    answer = [[0]*n for _ in range(n)]
    for start in range(n):
        visited = [False]*n
        q = deque([start])
        # visited[start] = True
        while q:
            s = q.popleft()
            for idx, c in enumerate(graph[s]):
                if c == 1 and not visited[idx]:
                    q.append(idx)
                    visited[idx] = True
                    answer[start][idx] = 1
                    # print(answer)
                # elif c == 0:
                #     visited[idx] = True
    return answer

answer = bfs(graph)
for i in answer:
    print(*i)