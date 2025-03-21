"""
시뮬레이션
방향 체크
사과 체크
길이 체크
"""
from collections import deque
import sys
input = sys.stdin.readline

# 보드
n = int(input())
board = [[0] * n for _ in range(n)]
board[0][0] = 's'

# 사과
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 'a' # 사과의 위치는 1부터 시작

# 방향 전환 정보
l = int(input())
directions = dict()
for _ in range(l):
    x, c = input().split()
    directions[int(x)] = c

dir_idx = 0
dx = [0,1,0,-1] # 우 하 좌 상
dy = [1,0,-1,0]

snake = deque([[0,0]])

time = 0
x,y = 0,0

while True:
    time += 1
    # 머리 이동
    nx = x + dx[dir_idx]
    ny = y + dy[dir_idx]

    # 벽 충돌
    if not (0 <= nx < n and 0 <= ny < n):
        break

    # 몸통 충돌
    if board[nx][ny] == 's':
        break

    # 이동
    if board[nx][ny] == 'a':
        board[nx][ny] = 's'
        snake.append([nx, ny])  # 머리 추가, 꼬리는 그대로 (길이 증가)
    else:
        board[nx][ny] = 's'
        snake.append([nx, ny])
        tx, ty = snake.popleft()  # 꼬리 제거
        board[tx][ty] = 0

    # 방향 전환
    if time in directions:
        if directions[time] == 'D':  # 오른쪽
            dir_idx = (dir_idx + 1) % 4
        else:  # 왼쪽
            dir_idx = (dir_idx - 1) % 4
    
    x,y = nx,ny

print(time)