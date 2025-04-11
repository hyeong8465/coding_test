import sys
import copy
sys.setrecursionlimit(100000)

# 방향: ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 초기 보드 설정
board = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        # [물고기 번호, 방향]
        board[i].append([data[2*j], data[2*j+1]-1])

max_score = 0

def find_fish(board, fish_number):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == fish_number:
                return (i, j)
    return None

def move_all_fishes(board, shark_x, shark_y):
    for fish_number in range(1, 17):
        position = find_fish(board, fish_number)
        if position is not None:
            x, y = position
            direction = board[x][y][1]
            for i in range(8):
                nd = (direction + i) % 8
                nx = x + dx[nd]
                ny = y + dy[nd]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == shark_x and ny == shark_y):
                        board[x][y][1] = nd
                        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                        break

def get_possible_positions(board, shark_x, shark_y):
    positions = []
    direction = board[shark_x][shark_y][1]
    x, y = shark_x, shark_y
    for i in range(4):
        x += dx[direction]
        y += dy[direction]
        if 0 <= x < 4 and 0 <= y < 4:
            if board[x][y][0] != 0:
                positions.append((x, y))
    return positions

def dfs(board, shark_x, shark_y, total):
    global max_score
    board = copy.deepcopy(board)

    total += board[shark_x][shark_y][0]
    board[shark_x][shark_y][0] = 0

    move_all_fishes(board, shark_x, shark_y)

    positions = get_possible_positions(board, shark_x, shark_y)
    if len(positions) == 0:
        max_score = max(max_score, total)
        return
    for next_x, next_y in positions:
        dfs(board, next_x, next_y, total)

dfs(board, 0, 0, 0)
print(max_score)