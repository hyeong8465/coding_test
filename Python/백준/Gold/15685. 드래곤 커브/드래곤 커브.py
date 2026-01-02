
n = int(input())
grid = [[0] * 101 for _ in range(101)]

# 우, 상, 좌, 하 (문제 정의에 따름)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    grid[y][x] = 1
    
    # 0세대 초기화
    curve_dirs = [d]
    
    # g세대까지 방향 리스트 확장 (핵심 로직)
    # 미리 방향만 반복문으로 만들어 둠
    for _ in range(g):
        # 현재까지의 경로를 역순으로 순회하며 +1 (90도 회전)
        next_dirs = []
        for curr_d in reversed(curve_dirs):
            next_dirs.append((curr_d + 1) % 4)
        curve_dirs.extend(next_dirs) # 리스트 확장
        
    # 결정된 전체 방향대로 이동하며 그리기
    for move_d in curve_dirs:
        nx, ny = x + dx[move_d], y + dy[move_d]
        grid[ny][nx] = 1
        x, y = nx, ny

# 정사각형 개수 세기
ans = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
            ans += 1
print(ans)