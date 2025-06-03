import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향: 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

while True:
    # 1. 현재 칸 청소
    if graph[x][y] == 0:
        graph[x][y] = 2
        ans += 1

    # 2. 주변 4칸 중 청소되지 않은 빈 칸이 있는지 확인
    cleaned = False
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 방향으로 회전
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            x, y = nx, ny
            cleaned = True
            break

    if cleaned:
        continue

    # 3. 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    back = (d + 2) % 4
    nx = x + dx[back]
    ny = y + dy[back]
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
        x, y = nx, ny
    else:
        break

print(ans)