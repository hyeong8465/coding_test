"""
23:54
bfs


"""
from collections import deque


def solution(maps):
    
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    q = deque([(0,0,1)])
    visited[0][0] = True
    while q:
        x,y,cnt = q.popleft()
        for i in range(4):
            for j in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if not visited[nx][ny] and maps[nx][ny] == 1:
                        if nx == n-1 and ny == m-1:
                            return cnt+1
                        q.append((nx,ny,cnt+1))
                        visited[nx][ny] = True
    return -1