"""
규칙
1. 조각은 한 번에 하나씩 채워넣음
2. 조각 회전 가능
3. 뒤집기 금지
4. 채워넣은 퍼즐조각과 인접한 칸이 비어있으면 안됨 -> 딱 맞아야 함

풀이
1. table에서 도형 추출
2. game_board에 회전해서 들어가는 걸 어떻게 확인할 것인가?
    - 회전을 어떻게 구현?

"""
from collections import deque

def bfs(x, y, my_map, target, visited): # target은 0/1
    row, col = len(my_map), len(my_map[0])

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    q = deque([(x,y)])
    visited[x][y] = True

    temp_blank = [(x,y)]
    min_row = x
    min_col = y

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0<=nr<row and 0<=nc<col and not visited[nr][nc]:
                if my_map[nr][nc] == target:
                    q.append((nr,nc))
                    visited[nr][nc] = True
                    temp_blank.append((nr,nc))
                    min_row = min(min_row, nr)
                    min_col = min(min_col, nc)
    blank = []
    for r, c in temp_blank:
        blank.append((r-min_row, c-min_col))
    # print(blank)
    return blank

def rotate(coords):
    max_row = 0 # col이 아니라 row 기준이어야 함
    for x, _ in coords:
        max_row = max(max_row, x)
            
    temp = []
    for x, y in coords:
        temp.append((y,max_row-x))
    return temp

    
def solution(game_board, table):
    row, col = len(game_board), len(game_board[0])

    # 빈칸 추출
    blanks = []
    visited = [[False]*col for _ in range(row)]
    for r in range(len(game_board)):
        for c in range(len(game_board[0])):
            if not visited[r][c] and game_board[r][c] == 0:
                blanks.append(bfs(r, c, game_board, 0, visited))

    # 도형 추출
    blocks = []
    visited = [[False]*col for _ in range(row)]
    for r in range(len(table)):
        for c in range(len(table[0])):
            if not visited[r][c] and table[r][c] == 1:
                blocks.append(bfs(r, c, table, 1, visited))

    # 회전과 같은가
    visited_blanks = [False]*len(blanks)
    visited_blocks = [False]*len(blocks)

    answer = 0
    for blank_i in range(len(blanks)):
        if visited_blanks[blank_i]:
            continue
        for block_i in range(len(blocks)):
            if visited_blocks[block_i]:
                continue
            if len(blanks[blank_i]) == len(blocks[block_i]):
                for _ in range(4):
                    if sorted(blanks[blank_i]) == sorted(blocks[block_i]): # 정렬되어 있음을 보장할 수 없음
                        visited_blocks[block_i] = True
                        visited_blanks[blank_i] = True

                        answer += len(blanks[blank_i])
                        break
                    blocks[block_i] = rotate(blocks[block_i])
            if visited_blanks[blank_i]: break

    print(answer)
    return answer