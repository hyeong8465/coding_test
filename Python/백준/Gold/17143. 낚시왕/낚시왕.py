####################### grids version #######################
def catch(fisher):
    for row in range(r):
        if grids[row][fisher]: # 빈 배열이 아니면
            _, _,z = grids[row][fisher] # 각 칸엔 상어가 한마리만 있음
            grids[row][fisher] = None
            return z # 바로 size return
    return 0

# 최적화 필요
# 최적화 전 시간복잡도 O(RxCxS) = 100x100x1000 = 1천만
# 최적화 아이디어: 사이클로 이동 횟수를 한번에 줄이자. 사이클의 나머지만큼만 시뮬
# 사이클: (row(좌우 이동) 혹은 col(상하 이동)의 길이 - 1) * 2
def move(grids): 
    new_grids = [[None] * c for _ in range(r)]
    for row in range(r):
        for col in range(c):
            if not grids[row][col]:
                continue
            s,d,z = grids[row][col]
            x, y = row, col
            # 이동
            if d in (1,2): # 상하
                cycle = (r-1)*2
                dist = s%cycle

                while dist > 0:
                    if d == 1:
                        if x - dist >= 0:
                            x -= dist
                            dist = 0
                        else:
                            dist -= x
                            x = 0
                            d = 2
                    else:
                        if x + dist < r:
                            x += dist
                            dist = 0
                        else:
                            dist -= (r-1-x)
                            x = r-1
                            d = 1
            
            else: # 좌우 이동
                cycle = (c-1)*2
                dist = s%cycle

                while dist > 0:
                    if d == 4:
                        if y - dist >= 0:
                            y -= dist
                            dist = 0
                        else:
                            dist -= y
                            y = 0
                            d = 3
                    else:
                        if y + dist < c:
                            y += dist
                            dist = 0
                        else:
                            dist -= (c-1-y)
                            y = c-1
                            d = 4
            
            if new_grids[x][y]:
                if new_grids[x][y][2] < z:
                    new_grids[x][y] = (s,d,z)
            else:
                new_grids[x][y] = (s,d,z)
    return new_grids

import sys
input = sys.stdin.readline

r,c,m = map(int, input().split())

grids = [[None] * c for _ in range(r)]

for _ in range(m):
    x,y,s,d,z = map(int, input().split()) # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
    grids[x-1][y-1] = (s,d,z)

# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
dx = [0,-1,1,0,0] 
dy = [0,0,0,1,-1]

ans = 0
for fisher in range(c):
    ans += catch(fisher)
    grids = move(grids)

print(ans)