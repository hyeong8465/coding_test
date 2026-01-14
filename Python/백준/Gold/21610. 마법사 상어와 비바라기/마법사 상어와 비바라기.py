"""
16:40

인덱스: 1 based
1 <-> N 연결

비바라기 시전: N,1를 포함해서 우, 상, 우상에 구름이 생김

구름 이동 m번: 방향, 거리
    방향: 8방향
    1. 모든 구름이 d방향으로 s만큼 이동
    2. 각 칸의 물의 양이 1씩 증가
    3. 구름 삭제
    4. 물복사버그: 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 바구니의 물 증가
        경계를 넘어가는 칸은 스킵
    5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에서 구름이 생기고 물의 양 -2
        3에서 구름의 도착지는 스킵 -> 어떻게 효율적으로 체크?
        큐에서 popleft한 것 저장하는 임시 배열 추가
물의 양의 합?

시뮬
"""
# from collections import deque

n, m = map(int, input().split())
baskets = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

clouds = [(n-1,0), (n-1,1), (n-2,0), (n-2,1)]

for _ in range(m):
    d, s = map(int, input().split())
    new_clouds = []
    departments = set()

    # move and rain
    for x, y in clouds:    
        nx, ny = (x+dx[d]*s)%n, (y+dy[d]*s)%n
        baskets[nx][ny] += 1
        departments.add((nx,ny))
    # print()
    # for b in baskets:
    #     print(*b)
    # print(departments)
    
    # water copy bug
    for x, y in departments:
        cnt = 0
        for i in [2,4,6,8]:
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and baskets[nx][ny] >= 1:
                cnt += 1
            # print(i, cnt, baskets[nx][ny])
        baskets[x][y] += cnt
    # print()
    # for b in baskets:
    #     print(*b)
    
    # make clouds
    # print(clouds)
    for i in range(n):
        for j in range(n):
            # print(i,j)
            if (i, j) in departments: continue
            if baskets[i][j] >= 2:
                baskets[i][j] -= 2
                new_clouds.append((i,j))
    # print()
    # for b in baskets:
    #     print(*b)
    
    clouds = new_clouds

ans = 0
for b in baskets:
    ans += sum(b)
print(ans)

            


        
    
    
    


