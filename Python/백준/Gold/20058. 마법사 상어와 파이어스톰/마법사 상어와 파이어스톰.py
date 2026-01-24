import sys
from collections import deque
input = sys.stdin.readline

# 2**N을 매번 계산하지 않고 변수로 저장
n_exp, q_count = map(int, input().split())
N = 1 << n_exp 
ices = [list(map(int, input().split())) for _ in range(N)]
l_list = list(map(int, input().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def rotate_subgrid(l):
    sub_size = 1 << l # 2^L
    new_ices = [[0] * N for _ in range(N)]
    
    # 격자 단위로 처리
    for y in range(0, N, sub_size):
        for x in range(0, N, sub_size):
            # 부분 격자 떼어내기
            chunk = [row[x:x+sub_size] for row in ices[y:y+sub_size]]
            
            # 90도 회전 (Pythonic way)
            rotated_chunk = list(map(list, zip(*chunk[::-1])))
            
            # 다시 붙이기
            for i in range(sub_size):
                for j in range(sub_size):
                    new_ices[y+i][x+j] = rotated_chunk[i][j]
    return new_ices

def melt_ice():
    melt_candidates = []
    for x in range(N):
        for y in range(N):
            if ices[x][y] == 0: continue
            
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and ices[nx][ny] > 0:
                    cnt += 1
            
            if cnt < 3:
                melt_candidates.append((x, y))
    
    # 동시에 녹이기
    for x, y in melt_candidates:
        ices[x][y] -= 1

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            # 범위 체크, 얼음 존재 여부, 방문 여부 확인
            if 0 <= nx < N and 0 <= ny < N:
                if ices[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

# --- Main Simulation ---
for l in l_list:
    # 1. 회전 (l이 0이면 회전해도 변화 없음 -> 최적화 가능하지만 그대로 둬도 무방)
    if l > 0:
        ices = rotate_subgrid(l)
    
    # 2. 얼음 녹이기
    melt_ice()

# --- Result Calculation ---
total_ice = sum(sum(row) for row in ices)
max_chunk = 0
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # [중요] 얼음이 있고 방문하지 않은 경우만 탐색
        if ices[i][j] > 0 and not visited[i][j]:
            max_chunk = max(max_chunk, bfs(i, j))

print(total_ice)
print(max_chunk)