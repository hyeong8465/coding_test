"""
12:02

M가지 색상
검: -1
무: 0
상하좌우 인접

블록 그룹:
    1. 일반 블록이 적어도 하나 이상
    2. 일반 블록의 색은 모두 같아야 함
    3. 검은색 포함 x
    4. 무지개는 상관 없음
    5. 블록의 갯수는 2개 이상
    기준 블록은 무지개 블록이 아닌 블록 중에서 행, 열의 번호가 가장 작은 블록

시뮬: 블록 그룹이 없을 때까지 반복
    1. 크기가 가장 큰 블록 찾음
        1. 무지개 블록의 수가 가장 많은 그룹
        2. 기준 블록의 행이 가장 큰 그룹
        3. 기준 블록의 열이 가장 큰 그룹
    2. 해당 블록 그룹의 모든 블록 제거, 블록의 수**2만큼의 점수 획득
    3. 격자에 중력 작용
    4. 격자 반시계방향 90도 회전
    5. 중력 적용

중력 적용: 검은 색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동

최종 점수는?

1초
time: 플레이 횟수
M번의 bfs, 2번의 중력
M*N**2+2*N**2 -> 2800
O(time*M*N**2+2*N**2) -> time*2800
time의 범위?

find_groups() -> best_group
    visited = [[False]*n for _ in range(n)]
    best_group = [(), ... ,()]
    1. 전체를 순회하면서 방문하지 않은 칸을 만나면, 해당 숫자와 위치를 기준으로 bfs로 그룹 확인
        - 포함된 무지개 색은 따로 list에 저장
    2. bfs로 그룹을 찾았으면 무지개 색 블록의 방문처리를 False로 롤백
    3. best_group의 길이보다 클 때만 best_group을 업데이트
        - 전체를 순차적으로 순회하고 있기 때문에 기준 블록의 행, 열 조건은 당연히 만족

rotation() -> rotated_matrix
    1. -2인 칸을 -1 혹은 다른 칸을 만날 때까지 swift
    2. 회전
    3. 중력
    


"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def find_groups(grid):
    visited = [[False] * n for _ in range(n)]
    
    best_group = []
    stats = [-1,-1,-1,-1]
    
    # 전체 순회
    for x in range(n):
        for y in range(n):
            if grid[x][y] > 0 and not visited[x][y]:
                
                # bfs 시작
                color = grid[x][y]
                q = deque([(x,y)])
                visited[x][y] = True
                
                rainbows = []
                normals = [(x,y)]

                while q:
                    r, c = q.popleft()
                    
                    for i in range(4):
                        nr, nc = r+dx[i], c+dy[i]
                        if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                            if grid[nr][nc] == 0 or grid[nr][nc] == color:
                                q.append((nr,nc))
                                visited[nr][nc] = True
                                if grid[nr][nc] == 0: # rainbow
                                    rainbows.append((nr,nc))
                                else:
                                    normals.append((nr,nc))
                
                for rainbow_x, rainbow_y in rainbows:
                    visited[rainbow_x][rainbow_y] = False

                total_blocks = len(normals) + len(rainbows)
                if total_blocks < 2:
                    continue

                normals.sort(key=lambda x:(x[0], x[1]))
                # print(normals)
                std_r, std_c = normals[0]

                current_stats = [total_blocks, len(rainbows), std_r, std_c]

                if current_stats > stats:
                    stats = current_stats
                    best_group = normals+rainbows
                
    # for v in visited:
    #     print(*v)    
    # print(best_group)
    return best_group

# O(N^2) 중력 함수 예시
def fall(grid):
    n = len(grid)
    for c in range(n):
        top = n - 1
        for r in range(n - 1, -1, -1):
            if grid[r][c] == -1:
                top = r - 1
            elif grid[r][c] >= 0:
                if r != top:
                    grid[top][c] = grid[r][c]
                    grid[r][c] = -2
                top -= 1
    return grid

score = 0
while True:
    # 조건을 만족하는 그룹 찾기
    best_group = find_groups(grid)
    
    # 그룹을 못 찾은 경우
    if len(best_group) == 0:
        break
    
    # 그룹을 찾은 경우
    # 블록 삭제
    score += len(best_group)**2
    for x, y in best_group:
        grid[x][y] = -2
    
    # print("불록삭제 후","===="*15)
    # for g in grid:
    #     print(*g)
    
    # 첫번째 fall
    grid = fall(grid)

    # print("첫번 째 fall","===="*15)
    # for g in grid:
    #     print(*g)

    # roation
    # grid = [list(i) for i in zip(*grid)][::-1]
    grid = list(map(list, zip(*grid)))[::-1]
    
    grid = fall(grid)
    
    # print("===="*15)
    # for g in grid:
    #     print(*g)

print(score)



"""
13:32

"""