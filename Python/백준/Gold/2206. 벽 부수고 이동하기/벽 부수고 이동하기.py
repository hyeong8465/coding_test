from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

start = (0,0)
end = (n-1,m-1)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(start, end):
    x,y = start
    q = deque([(x,y,False,1)])
    visited = [[[False]*2 for _ in range(m)]  for _ in range(n)] # nxmx2(안뚫, 뚫)
    visited[x][y][0] = True

    while q:
        x,y,z,dis = q.popleft()

        if x == end[0] and y == end[1]:
            return dis
        
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]
            if 0<=px<n and 0<=py<m:
                if arr[px][py] == 0 and not visited[px][py][z]: # 벽이 아니고 벽을 부순적이 없으면
                    q.append((px,py,z,dis+1))
                    visited[px][py][z] = True
                elif arr[px][py] == 1 and z == 0 and not visited[px][py][1]:
                    q.append((px,py,1, dis+1))
                    visited[px][py][1] = True
    return -1

print(bfs(start, end))
