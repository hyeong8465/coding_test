"""
10:11
bfs + 브루트포스?
64C3 = 41664

"""
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
empty = []
virus = []
wall = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 0:
            empty.append((i,j))
        elif temp[j] == 2:
            virus.append((i,j))
        else:
            wall += 1


    graph.append(temp)

cands = list(combinations(empty, 3))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(graph):
    visited = [[False]*m for _ in range(n)]
    for v in virus:
        start = v
        q = deque([start])
        visited[start[0]][start[1]] = True

        while q:
            x,y = q.popleft()
            for i in range(4):
                px = x+dx[i]
                py = y+dy[i]
                if 0<=px<n and 0<=py<m:
                    if graph[px][py] == 0:
                        if not visited[px][py]:
                            graph[px][py] = 2
                            q.append((px,py))
                            visited[px][py] = True
    # for g in graph:
    #     print(g)
    # print('='*12)
    return graph

result = 0
for cand in cands:
    graph_copy = [g[:] for g in graph]

    for c in cand:
        graph_copy[c[0]][c[1]] = 1 # 벽을 만듦

    # for g in graph_copy:
    #     print(g)

    # print(bfs(graph_copy))
    graph_copy = bfs(graph_copy)
    # for g in graph_copy:
    #     print(g)

    temp = 0
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 0:
                temp += 1
    # print(temp)
    # if result < temp:
    #     for g in graph_copy:
    #         print(g)

    result = max(result, temp)

print(result)
    





        

    



