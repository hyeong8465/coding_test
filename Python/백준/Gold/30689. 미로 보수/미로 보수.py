import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(input().rstrip()) for _ in range(n)]
cost = [list(map(int, input().split())) for _ in range(n)]

# R, D, L, U
dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
visited = [[0]*m for _ in range(n)]  # 0=미방문, 1=방문완료, 2=순환 탐색중
on_path = [[False]*m for _ in range(n)]  # 현재 DFS 스택 상의 노드
ans = 0

def dfs(x, y, path):
    global ans

    visited[x][y] = 1
    on_path[x][y] = True
    path.append((x, y))

    dx, dy = dirs[miro[x][y]]
    nx, ny = x + dx, y + dy

    if not (0 <= nx < n and 0 <= ny < m):
        pass  # 탈출
    elif visited[nx][ny] == 0:
        dfs(nx, ny, path)
    elif on_path[nx][ny]:
        # 루프 감지됨 → 루프 구간 추출
        loop = []
        found = False
        for px, py in path:
            if (px, py) == (nx, ny):
                found = True
            if found:
                loop.append((px, py))
        min_cost = min(cost[x][y] for x, y in loop)
        ans += min_cost

    path.pop()
    on_path[x][y] = False

# 전체 탐색
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            dfs(i, j, [])

print(ans)