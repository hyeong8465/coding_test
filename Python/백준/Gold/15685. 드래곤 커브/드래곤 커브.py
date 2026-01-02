"""
10:28
k 세대 드래곤 커브는 k-1 세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝점에 붙인 것
100x100에서 1x1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수

세대가 추가되면 이동한 만큼 또 이동 -> 재귀
구현
1초

재귀 형태로 지금까지의 이동을 쌓아두고 세대가 k랑 같아질때까지 수행
드래콘 커브를 전부 표시해두고, 조건을 만족하는 정사각형 갯수 카운트


격자 밖으로 벗어는 경우는 없음
겹칠 수 있음

이동 방향
0: 0
1: 0-1
2: 0-1/2-1
3: 0-1-2-1/2-4-2-1

좌표
0: (0,0) - (1,0)
1: (0,0) - (1,0) - (1,-1)
2: (0,0) - (1,0) - (1,-1) - (0,-1) - (0,-2)
(0,-1), (-1,-2)
3: (0,0) - (1,0) - (1,-1) - (0,-1) - (0,-2) - (-1,-2) - (-1,-1) - (-2,-1) - (-2,-2)

"""
n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]

dy = [0,-1,0,1] # row
dx = [1,0,-1,0] # col

grid = [[0]*101 for _ in range(101)]

def dfs(x, y, d, now_g, target_g, paths):
    if now_g > target_g:
        return
    
    if now_g == 0:
        grid[y][x] = 1
        nx = x+dx[d]
        ny = y+dy[d]
        grid[ny][nx] = 1
        # for g in grid:
        #     print(*g)
        paths.append(d)
        dfs(nx, ny, d, now_g+1, target_g, paths)
    else:  
        # print(111)
        # paths_copy = paths[:]
        nx = x
        ny = y
        # print(paths)
        for i in range(len(paths)-1, -1, -1):
            path = paths[i]
            nd = (path+1)%4
            # print(nd)
            nx = nx+dx[nd]
            ny = ny+dy[nd]
            grid[ny][nx] = 1
            paths.append(nd)
        # for g in grid:
            # print(*g)        
        dfs(nx, ny, d, now_g+1, target_g, paths)    

# dfs(5,5,0,0,2,[])

for curve in curves:
    x,y,d,g = curve
    dfs(x,y,d,0,g,[])

ans = 0
dx = [0,1,0,1]
dy = [0,0,1,1]
for i in range(100):
    for j in range(100):
        cnt = 0
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if grid[nx][ny] == 1:
                cnt += 1
            
        if cnt == 4:
            # print(i,j)
            ans += 1

print(ans)
    






