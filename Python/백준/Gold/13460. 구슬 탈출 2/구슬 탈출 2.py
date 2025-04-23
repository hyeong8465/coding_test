"""
09:20

빨간 공만 구멍에 들어가야 함

상하좌우 방향을 먼저 찾아야 함
bfs로 방향 전환 지점을 찾는다?
백트래킹?
더 많이 이동한 구슬이 더 늦게 도착한 것

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':
            rx,ry = i,j
        elif graph[i][j] == 'B':
            bx,by = i,j

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(rx, ry, bx, by):
    q = deque([(rx, ry, bx, by,0)])
    
    visited = []
    visited.append((rx,ry,bx,by))

    while q:
        # 지금 위치
        rx, ry, bx, by,cnt = q.popleft()
        # 10번 넘으면 -1 출력
        if cnt > 10:
            return -1
        
        # 구멍 도착
        if graph[rx][ry] == 'O':
            return cnt
        
        # 상하좌우 이동
        for i in range(4):
            prx, pry, pbx, pby = rx, ry, bx, by # 지금 위치
            while True:
                prx += dx[i]
                pry += dy[i]
                # 빨간공 이동
                if graph[prx][pry] == '#':
                    prx -= dx[i]
                    pry -= dy[i]
                    break
                if graph[prx][pry] == 'O':
                    break
            # 파란공 이동
            while True:
                pbx += dx[i]
                pby += dy[i]
                if graph[pbx][pby] == '#':
                    pbx -= dx[i]
                    pby -= dy[i]
                    break
                if graph[pbx][pby] == 'O':
                    break
            
            if graph[pbx][pby] == 'O':
                continue
            if prx == pbx and pry == pby:
                if abs(prx-rx) + abs(pry-ry) > abs(pbx-bx) + abs(pby-by):
                    prx -= dx[i]
                    pry -= dy[i]
                else:
                    pbx -= dx[i]
                    pby -= dy[i]
            if (prx, pry, pbx, pby) not in visited:
                q.append((prx, pry, pbx, pby, cnt+1))
                visited.append((prx, pry, pbx, pby))
    return -1
                
print(bfs(rx,ry,bx,by))