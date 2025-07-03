"""
17:33
bfs, 백트래킹

집까지 도착하는 경우 중 거리가 K인 가짓수
"""
r, c, k = map(int, input().split())

arr = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
visited[r-1][0] = True

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0
def bfs(x,y,cnt):
    global ans
    if cnt == k:
        if x == 0 and y == c-1:
            ans += 1
        else:
            return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if arr[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                bfs(nx, ny, cnt+1)
                visited[nx][ny] = False

bfs(r-1,0,1)
print(ans)