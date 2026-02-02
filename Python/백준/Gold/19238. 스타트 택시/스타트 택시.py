# gemini 최적화
from collections import deque
import sys
input = sys.stdin.readline

n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

x, y = map(int, input().split())
x -= 1
y -= 1

customers = {}
for _ in range(m):
    sr, sc, er, ec = map(int, input().split())
    customers[(sr-1, sc-1)] = (er-1, ec-1)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def find_customer(start_x, start_y):
    # 시작 위치에 바로 승객이 있는 경우 (거리 0)
    if (start_x, start_y) in customers:
        return (start_x, start_y, 0)
    
    visited = [[False] * n for _ in range(n)]
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    
    candidates = []
    min_dist = float('inf') # 최단 거리 기록용

    while q:
        cx, cy, dist = q.popleft()
        
        # [최적화] 이미 찾은 최단 거리보다 더 멀리 가려고 하면 탐색 중단
        if dist >= min_dist:
            break

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = True
                    if (nx, ny) in customers:
                        # 승객 발견
                        min_dist = dist + 1
                        candidates.append((nx, ny, dist + 1))
                    else:
                        q.append((nx, ny, dist + 1))
    
    if not candidates:
        return None
    
    # 거리 -> 행 -> 열 순서 정렬
    candidates.sort(key=lambda x: (x[2], x[0], x[1]))
    return candidates[0]

def find_destination(start_x, start_y, end_x, end_y):
    visited = [[False] * n for _ in range(n)]
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    
    while q:
        cx, cy, dist = q.popleft()
        
        if cx == end_x and cy == end_y:
            return dist
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
    return -1

# Main Logic
for _ in range(m):
    # 1. 최단 거리 승객 찾기
    result = find_customer(x, y)
    
    if result is None:
        print(-1)
        quit()
        
    start_x, start_y, dist = result
    
    # 2. 승객에게 이동 (연료 체크)
    # [수정] 이동할 거리가 연료보다 많으면 실패 (같으면 성공)
    if fuel - dist < 0:
        print(-1)
        quit()
        
    fuel -= dist
    end_x, end_y = customers[(start_x, start_y)]
    del customers[(start_x, start_y)] # 탑승한 승객 목록에서 제거
    
    # 3. 목적지로 이동
    dist_to_dest = find_destination(start_x, start_y, end_x, end_y)
    
    if dist_to_dest == -1: # 목적지 도달 불가
        print(-1)
        quit()
        
    # [수정] 이동할 거리가 연료보다 많으면 실패 (같으면 성공)
    if fuel - dist_to_dest < 0:
        print(-1)
        quit()
        
    fuel -= dist_to_dest
    
    # 4. 연료 충전 (소모한 연료의 2배 충전)
    fuel += dist_to_dest * 2
    
    # 택시 위치 갱신
    x, y = end_x, end_y

print(fuel)