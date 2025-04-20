from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def get_exposed_cheese():
    visited = [[False]*m for _ in range(n)]
    air = deque()
    air.append((0, 0))
    visited[0][0] = True

    contact = [[0]*m for _ in range(n)]
    melt = []

    while air:
        x, y = air.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    air.append((nx, ny))
                elif board[nx][ny] == 1:
                    contact[nx][ny] += 1
                    if contact[nx][ny] == 2:
                        melt.append((nx, ny))
    return melt

hour = 0
while True:
    melt = get_exposed_cheese()
    if not melt:
        break
    for x, y in melt:
        board[x][y] = 0
    hour += 1

print(hour)