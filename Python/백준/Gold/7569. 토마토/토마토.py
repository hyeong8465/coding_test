import sys
from collections import deque

m,n,h = map(int, input().split()) # n행, m열, h높이
arr = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        arr[i].append(list(map(int, input().split())))

def bfs():
    visited = [[[False]*m for _ in range(n)] for _ in range(h)]
    q = deque() # h,n,m
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    q.append((i,j,k,0)) # h, row, col, day
                    visited[i][j][k] = True
                elif arr[i][j][k] == -1:
                    visited[i][j][k] = True
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    dh = [-1, 1]

    while q:
        he, ro, co, day = q.popleft()
        for i in range(4): # 상, 하, 좌, 우
            pro, pco = ro+dx[i], co+dy[i]
            if -1 < pro < n and -1<pco<m:
                if arr[he][pro][pco] == 0 and not visited[he][pro][pco]:
                    q.append((he, pro, pco, day+1))
                    visited[he][pro][pco] = True
            else:
                continue
        for i in range(2):
            phe = he + dh[i]
            if -1 < phe < h:
                if arr[phe][ro][co] == 0 and not visited[phe][ro][co]:
                    q.append((phe, ro, co, day+1))
                    visited[phe][ro][co] = True

    sum_val = 0
    for v1 in visited:
        for v2 in v1:
            sum_val += sum(v2)
    if sum_val != h*n*m:
        print(-1)
    else:
        print(day)

bfs()