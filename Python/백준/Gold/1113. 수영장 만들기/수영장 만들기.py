from collections import deque
n, m = map(int, input().split())
pool = [list(map(int, list(input()))) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(a,b):
    q = deque([(a,b)])
    visited = [[False]*m for _ in range(n)]
    visited[a][b] = True
    
    minipool = [(a,b)]
    
    h = pool[a][b]
    min_h = 10
    
    global answer
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            px, py = x+dx[i], y+dy[i]
            
            if not (0<=px<n and 0<=py<m):
                return 0,0
            
            if not visited[px][py]:
                if pool[px][py] <= h:
                    q.append((px,py))
                    visited[px][py] = True
                    minipool.append((px,py))
                else:
                    min_h = min(min_h, pool[px][py])
    # print(minipool, min_h)
    
    for mini in minipool:
        x,y = mini
        answer += (min_h-pool[x][y])
        pool[x][y] = min_h

answer = 0

for i in range(n):
    for j in range(m):
        bfs(i,j)
print(answer)