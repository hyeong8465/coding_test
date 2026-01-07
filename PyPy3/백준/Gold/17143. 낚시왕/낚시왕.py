import sys
input = sys.stdin.readline

def catch(fisher):
    for row in range(r):
        if grids[row][fisher]: # 상어 발견
            _, _, z = grids[row][fisher]
            grids[row][fisher] = None # [수정] 상어를 격자에서 삭제 (None 처리)
            return z # 잡은 상어 크기 반환
    return 0

def move(grids): 
    # 매 턴마다 새로운 판 생성 (None 초기화는 매우 빠름)
    new_grids = [[None] * c for _ in range(r)]
    
    for row in range(r):
        for col in range(c):
            if not grids[row][col]:
                continue
            
            s, d, z = grids[row][col]
            x, y = row, col
            
            # --- 이동 로직 (cycle 최적화 적용) ---
            if d in (1, 2): # 상(1), 하(2)
                cycle = (r - 1) * 2
                if s >= cycle: s %= cycle # 1000번 이동을 최대 2*R번으로 단축
                
                # 남은 거리만큼 시뮬레이션 (충분히 빠름)
                for _ in range(s):
                    if d == 1 and x == 0: d = 2
                    elif d == 2 and x == r - 1: d = 1
                    x += dx[d]
                    
            else: # 우(3), 좌(4)
                cycle = (c - 1) * 2
                if s >= cycle: s %= cycle

                for _ in range(s):
                    if d == 4 and y == 0: d = 3
                    elif d == 3 and y == c - 1: d = 4
                    y += dy[d]
            
            # --- Eat 로직 통합 ---
            # 이동할 위치에 상어가 없거나, 내가 더 크면 덮어쓰기
            if not new_grids[x][y] or new_grids[x][y][2] < z:
                new_grids[x][y] = (s, d, z)
            # 내가 더 작으면? 그냥 덮어쓰지 않음 (자동으로 사라짐)

    return new_grids

# --- 메인 ---
r, c, m = map(int, input().split())

grids = [[None] * c for _ in range(r)]

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    # (x-1, y-1) 좌표 보정
    grids[x-1][y-1] = (s, d, z)

dx = [0, -1, 1, 0, 0] 
dy = [0, 0, 0, 1, -1]

ans = 0
for fisher in range(c):
    ans += catch(fisher)
    grids = move(grids)

print(ans)