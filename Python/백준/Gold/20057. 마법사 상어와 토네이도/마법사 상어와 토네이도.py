"""
09:30

격자 가운데에서 좌-하-우-상 토네이도 이동

토네이도가 한 칸 이동할 때, 날리는 모래
이동하는 칸의 모래가 비율만큼 날리고(소수점 아래 버림), 알파로 이동하는 모래의 양은 나머지 모래의 양
이동 방향에 따라 비율 회전

격자 밖으로 나간 모래의 양?

시뮬 O(N**2*10) -> 250만

1. 토네이도 이동
    1-1 -2-2 -3-3-4-4-5-5-6
    좌-하-우-상-좌-하

    거리는 2칸씩 증가


2. 모래 날림

 0-1-x-1-0
 2-7-y-7-2
0-10-a-10-0
--   5

"""

# 좌-하-우-상
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# ratio가 0이면 alp
dir_to_ratio = {
    0: [(0,-3,0.05), (-1,-2,0.1), (-2,-1,0.02), (-1,-1,0.07), (-1,0,0.01), (1,-2,0.1), (2,-1,0.02), (1,-1,0.07),(1,0,0.01), (0,-2,0)],
    1: [(0,-1,0.01), (1,-2,0.02), (1,-1,0.07), (2,-1,0.1), (3,0,0.05), (0,1,0.01), (1,2,0.02), (1,1,0.07), (2,1,0.1),(2,0,0)],
    2: [(0,3,0.05), (-1,2,0.1), (-2,1,0.02), (-1,1,0.07), (-1,0,0.01), (1,2,0.1), (2,1,0.02), (1,1,0.07),(1,0,0.01), (0,2,0)],
    3: [(0,-1,0.01), (-1,-2,0.02), (-1,-1,0.07), (-2,-1,0.1), (-3,0,0.05), (0,1,0.01), (-1,2,0.02), (-1,1,0.07), (-2,1,0.1),(-2,0,0)]
} # 시작점 기준, (dx,dy,ratio)


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

x = n//2
y = x
d = 0
cnt = 1
ans = 0

while True:
    # print(x,y)
    if (x,y) == (0,0):
        break

    # 이동
    for _ in range(cnt):
        
        nx, ny = x+dx[d], y+dy[d]
        sand = grid[nx][ny]
        
        # 모래 날림
        replaced_sand = 0
        for sand_dx, sand_dy, ratio in dir_to_ratio[d]:
            
            nnx, nny = x+sand_dx, y+sand_dy
            amount = int(sand*ratio)
            replaced_sand += amount
            
            if not (0<=nnx<n and 0<=nny<n):
                if ratio == 0:
                    ans += sand-replaced_sand
                else:
                    ans += amount
                # print(ans)
                continue

            if ratio == 0: # ratio가 0인 경우가 for문 가장 마지막에 와서 순서 괜찮음
                grid[nnx][nny] += sand-replaced_sand
            else:
                grid[nnx][nny] += amount
        
        grid[nx][ny] = 0
        
        # for g in grid:
        #     print(*g)
        # print("==========")
        
        x, y = nx, ny
        if (x,y) == (0,0):
            break
    
    if d in [1,3]:
        cnt += 1
    
    d = (d+1)%4
    
print(ans)
    
        
