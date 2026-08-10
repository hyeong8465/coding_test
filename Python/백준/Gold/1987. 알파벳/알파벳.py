from collections import deque
import sys
input = sys.stdin.readline

row,col = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(row)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# def bfs(start):
#     x,y = start
#     q = deque([(x, y, set(graph[x][y]))])
#     route = set()
#     route.add(start)
#     res = 1

#     while q:
#         x, y, r = q.popleft()
#         # print(x,y,r)
#         res = max(res, len(r))

#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0<=nx<row and 0<=ny<col:
#                 if graph[nx][ny] not in r:
#                     temp = r.copy()
#                     temp.add(graph[nx][ny])
#                     q.append((nx,ny,temp))
#                     # route.add()
#     print(res)
# bfs((0,0))

res = 1
def dfs(node, route):
    x,y = node

    global res
    res = max(res, len(route))

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<row and 0<=ny<col:
            if graph[nx][ny] not in route:
                temp = route.copy()
                temp.add(graph[nx][ny])
                dfs((nx,ny), temp)
    # print(res)
a = set(graph[0][0])
dfs((0,0), a)
print(res)