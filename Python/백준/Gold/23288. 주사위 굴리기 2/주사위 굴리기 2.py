"""
11:11
1-based index

1. 이동방향으로 한칸 굴러감, 이돝 방향에 칸이 없다면, 이동방향 반대로, 한칸 구름
2. 도착한 칸에 대한 점수 획득
3. 이동 방향 결정(A = 주사위 아랫면 정수, B = 도착한 칸에 있는 정수)
    1. A>B: 이동 방향 시계방향 90도 회전
    2. A<B: 이동 방향 반시계방향 90도 회전
    3. A=B: 변화 없음

칸에 대한 점수: B*C
    B = (x,y)에 있는 정수 B
    C = (x,y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수
    단, 이동할 수 있는 칸에는 모두 정수 B가 있어야 함
-> BFS

1. 이동 방향으로 이동
2. B값을 기준으로 BFS
3. 점수 계산 및 합산
4. 주사위 및 이동 방향 업데이트 -> 주사위 회전을 어떻게 구현?
    1. 미리 하드코딩 -> 주사위가 회전해서 도착할 수도 있어서 하드코딩 불가
        같은 5더라도, 진행했던 경로에 따라 상하좌우 칸의 값이 다름
        6-3-5 vs. 6-5
    2. [북,동,남,서,상,하]
        2-1. 북으로 이동
            [상, 동, 하, 서, 남, 북]
    
시간 복잡도: 240만
이동 횟수: 1000
BFS: 20**2
주사위 업데이트: 6

"""
from collections import deque

# 입력
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 함수
def roll(dice, dir):
    a, b, c, d, e, f = dice
    if dir == 0:  # 북
        return [a,b,e,f,d,c]
    elif dir == 1:  # 동
        return [e,f,c,d,b,a]
    elif dir == 2:  # 남
        return [a,b,f,e,c,d]
    elif dir == 3:  # 서
        return [f,e,c,d,a,b]

# score
def bfs():
    score = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if score[i][j]: continue

            s = grid[i][j]
            store = []
            q = deque([(i,j)])
            score[i][j] = True
            
            while q:
                x, y = q.popleft()
                store.append((x,y))

                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<n and 0<=ny<m and not score[nx][ny] and grid[nx][ny] == s:
                        q.append((nx,ny))
                        score[nx][ny] = True
            
            cnt = len(store)
            for x,y in store:
                score[x][y] = cnt

    return score

# init
x,y = 0, 0
direction = 1 # 동쪽
dice = [3,4,2,5,1,6] # 주사위 전개도 - 동서북남상하 순으로 기입

# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# main
ans = 0
score = bfs()
for _ in range(k):
    
    # 1. 이동
    nx, ny = x+dx[direction], y+dy[direction]
    if 0<=nx<n and 0<=ny<m:
        x, y = nx, ny
    else:
        direction = (direction + 2)%4
        x, y = x+dx[direction], y+dy[direction]
    # print(x,y)
    
    dice = roll(dice, direction)
    a = dice[-1]

    # 2. 점수 계산 및 합산
    b = grid[x][y]
    c = score[x][y]
    ans += b*c
    # print(a,b,c, ans)

    # 3. 이동방향 업데이트
    # print(direction)
    if a > b:
        direction = (direction+1)%4
    elif a < b:
        direction = (direction-1)%4
        # print(222)
    # print(direction)

print(ans)
