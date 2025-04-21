import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 궁수 공격 함수 (BFS)
def bfs(sx, sy, temp_board):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((sx, sy, 1))
    dx = [0, -1, 0]  # 좌 → 상 → 우 (왼쪽 우선)
    dy = [-1, 0, 1]
    
    while q:
        x, y, dist = q.popleft()
        if dist > d: # 사정거리를 넘어가면 break
            break
        if 0 <= x < n and 0 <= y < m and temp_board[x][y] == 1: # 보드 안에 있고 적이면 바로 출력
            return (x, y)
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist+1))
    return None

# 궁수 조합마다 시뮬레이션
answer = 0
for archers in combinations(range(m), 3):
    temp_board = copy.deepcopy(board)
    result = 0
    
    for _ in range(n):
        targets = set()
        for archer in archers:
            t = bfs(n-1, archer, temp_board)
            if t:
                targets.add(t)
        # 적 제거
        for x, y in targets:
            if temp_board[x][y] == 1:
                temp_board[x][y] = 0
                result += 1
        # 적 이동
        temp_board.pop() # 맨 아랫줄 빼고
        temp_board.insert(0, [0]*m) # 위에 추가
    answer = max(answer, result)

print(answer)