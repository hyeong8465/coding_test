import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    union = [(x, y)] # 연합 국가들의 좌표 리스트
    total_population = graph[x][y] # 연합의 총 인구수
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(graph[cx][cy] - graph[nx][ny])
                if l <= diff <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += graph[nx][ny]
    
    return union, total_population

days = 0

while True:
    visited = [[False] * n for _ in range(n)]
    is_moved = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total_pop = bfs(i, j, visited)
                
                # 연합이 2개 이상 모였을 때만 인구 이동 처리
                if len(union) > 1:
                    is_moved = True
                    new_pop = total_pop // len(union)
                    for ux, uy in union:
                        graph[ux][uy] = new_pop
    
    if not is_moved:
        break
    days += 1

print(days)