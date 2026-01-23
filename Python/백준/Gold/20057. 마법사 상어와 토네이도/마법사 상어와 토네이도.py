import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 좌, 하, 우, 상 (토네이도 진행 방향)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # 1. 좌측 방향(0)일 때 'y' 기준 모래가 퍼지는 상대 좌표 (x, y, ratio)
    # 비율이 0인 것은 알파(a) 위치를 의미함
    left_spread = [
        (-1, 1, 0.01), (1, 1, 0.01),  # 1%
        (-1, 0, 0.07), (1, 0, 0.07),  # 7%
        (-2, 0, 0.02), (2, 0, 0.02),  # 2%
        (-1, -1, 0.1), (1, -1, 0.1),  # 10%
        (0, -2, 0.05),                # 5%
        (0, -1, 0)                    # Alpha (a)
    ]

    # 2. 4방향 확산 패턴 미리 생성 (90도 반시계 회전: x, y -> -y, x)
    spreads = [[] for _ in range(4)]
    spreads[0] = left_spread
    
    for i in range(1, 4):
        for bx, by, ratio in spreads[i-1]:
            spreads[i].append((-by, bx, ratio))

    ans = 0
    x, y = N // 2, N // 2 # 시작점 (가운데)
    d = 0 # 현재 방향
    move_len = 1 # 이동 거리
    moved_cnt = 0 # 같은 거리로 이동한 횟수

    while True:
        if x == 0 and y == 0: break

        for _ in range(move_len):
            nx, ny = x + dx[d], y + dy[d]
            sand = grid[nx][ny]
            grid[nx][ny] = 0
            
            spread_total = 0
            
            # 현재 방향(d)에 맞는 확산 패턴 적용
            for sx, sy, ratio in spreads[d]:
                target_x, target_y = nx + sx, ny + sy
                
                # 알파(ratio 0)인지 확인
                if ratio == 0:
                    amount = sand - spread_total
                else:
                    amount = int(sand * ratio)
                    spread_total += amount
                
                # 격자 내부면 누적, 외부면 정답(ans)에 추가
                if 0 <= target_x < N and 0 <= target_y < N:
                    grid[target_x][target_y] += amount
                else:
                    ans += amount
            
            x, y = nx, ny
            if x == 0 and y == 0: break
        
        # 방향 전환 및 이동 길이 조정
        d = (d + 1) % 4
        moved_cnt += 1
        if moved_cnt == 2:
            move_len += 1
            moved_cnt = 0

    print(ans)

solve()