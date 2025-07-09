"""
09:42
시뮬레이션?

1. 미세먼지가 인접 칸에 확산
    공기청정기가 있는 칸엔 확산 불가
    확산량: 미세먼지//5
2. 공기청정기 작동
    반시계 / 시계 방향으로 먼지 이동
    공기 청정기로 들어가면 모두 정화

확산을 어떻게 한번에 할 수 있게 구현하지?
매번 새로 쓰기?
O(R*C*1000) 가능하겠는데
"""
r, c, t = map(int, input().split())
room = []
cond = None
for i in range(r):
    temp = list(map(int, input().split()))
    # print(temp)
    room.append(temp)
    if not cond:
        for j in range(c):
            if temp[j] == -1:
                cond = [(i,j), (i+1,j)]
cond1 = cond[0]
cond2 = cond[1]

# 하, 우, 상, 좌
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 1. 확산
def diver(room):
    ans = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] != 0 and room[i][j] != -1:
                cnt = 0
                val = room[i][j]//5
                for k in range(4): # 인접칸 확인
                    ni, nj = i+dx[k], j+dy[k]
                    if 0<=ni<r and 0<=nj<c and room[ni][nj] != -1:
                        cnt +=1
                        ans[ni][nj] += val
                ans[i][j] += room[i][j]-val*cnt
    ans[cond1[0]][cond1[1]] = -1
    ans[cond2[0]][cond2[1]] = -1
    return ans

# 2. 바람
def wind(room, cond1, cond2, R, C):
    # 1. 윗 부분 공기청정기 (반시계 방향)
    # (cond1[0], cond1[1]) 에서 시작
    
    # 공기청정기 바로 옆 칸의 먼지 (나중에 공기청정기로 들어갈 먼지)를 0으로 만듦
    # 실제로는 공기청정기에서 바람이 나와 그 다음칸을 비우는 것이므로,
    # 공기청정기 바로 다음칸부터 시작하여 한 칸씩 당겨오는 방식으로 구현
    
    # 1-1. 오른쪽으로 이동 (공기청정기 오른쪽 칸부터 시작)
    r_top, c_top = cond1[0], cond1[1]
    prev_dust = 0 # 공기청정기에서 나오는 바람은 0
    
    # 첫 줄 오른쪽으로 이동: (r_top, c_top+1) -> (r_top, c_top)
    #                      (r_top, c_top+2) -> (r_top, c_top+1) ...
    for j in range(c_top + 1, C):
        curr_dust = room[r_top][j]
        room[r_top][j] = prev_dust
        prev_dust = curr_dust

    # 1-2. 위쪽으로 이동 (맨 오른쪽 위 칸까지)
    # (r_top-1, C-1) -> (r_top, C-1) ... (0, C-1) -> (1, C-1)
    for i in range(r_top - 1, -1, -1):
        curr_dust = room[i][C - 1]
        room[i][C - 1] = prev_dust
        prev_dust = curr_dust
        
    # 1-3. 왼쪽으로 이동 (맨 위쪽 왼쪽 칸까지)
    # (0, C-2) -> (0, C-1) ... (0, 0) -> (0, 1)
    for j in range(C - 2, -1, -1):
        curr_dust = room[0][j]
        room[0][j] = prev_dust
        prev_dust = curr_dust

    # 1-4. 아래쪽으로 이동 (공기청정기 바로 윗 칸까지)
    # (1, 0) -> (0, 0) ... (r_top-1, 0) -> (r_top-2, 0)
    for i in range(1, r_top):
        curr_dust = room[i][0]
        room[i][0] = prev_dust
        prev_dust = curr_dust
    
    # 2. 아랫 부분 공기청정기 (시계 방향)
    # (cond2[0], cond2[1]) 에서 시작
    r_bottom, c_bottom = cond2[0], cond2[1]
    prev_dust = 0 # 공기청정기에서 나오는 바람은 0

    # 2-1. 오른쪽으로 이동
    for j in range(c_bottom + 1, C):
        curr_dust = room[r_bottom][j]
        room[r_bottom][j] = prev_dust
        prev_dust = curr_dust
        
    # 2-2. 아래쪽으로 이동
    for i in range(r_bottom + 1, R):
        curr_dust = room[i][C - 1]
        room[i][C - 1] = prev_dust
        prev_dust = curr_dust

    # 2-3. 왼쪽으로 이동
    for j in range(C - 2, -1, -1):
        curr_dust = room[R - 1][j]
        room[R - 1][j] = prev_dust
        prev_dust = curr_dust

    # 2-4. 위쪽으로 이동
    for i in range(R - 2, r_bottom, -1):
        curr_dust = room[i][0]
        room[i][0] = prev_dust
        prev_dust = curr_dust

    # 공기청정기 위치는 -1로 유지
    room[cond1[0]][cond1[1]] = -1
    room[cond2[0]][cond2[1]] = -1

    return room
# def wind(room, ud):
#     if ud == 'u':
#         a = cond1
#         x,y = cond1
#         direction = 1
#         idx = 2
#     else:
#         a = cond2
#         x,y = cond2
#         direction = -1
#         idx = 0
#     val = 0
#     while True:
#         nx, ny = x+dx[idx], y+dy[idx]
#         if (nx, ny) == a:
#             break
        
#         if 0<=nx<r and 0<=ny<c:
#             print(nx,ny)
#             val, room[nx][ny] = room[nx][ny], val
#             x, y = nx, ny
        
#         else:
#             idx = (abs(idx+direction))%4
#         # print(nx,ny)
#     return room

for _ in range(t):
    room = diver(room)
    room = wind(room,cond1, cond2,r, c)

ans = 0
for i in range(r):
    for j in range(c):
        ans += room[i][j]
print(ans+2)