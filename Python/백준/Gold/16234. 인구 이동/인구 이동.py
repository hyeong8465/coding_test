"""
11:04 -> 11:49
아래 방법에 의해 인구 이동이 없을 때까지 지속
1. 국경선을 공유하는 두 나라의 인구 차이가 l명 이상, r명 이하라면, 국경선 오픈
2. 국경선 열고 이동 시작
3. 국경선이 열러 있어 인접한 칸만을 이용해 이동할 수 있으면 그 나라는 오늘 하루 연합
4. 연합을 이루는 각 칸의 인구수는 연합의 인구수/연합을 이루는 칸의 수. 소수점 버림
5. 연합 해제, 국경선 닫음

연합 찾기 -> 분배

시뮬, dfs?
시간 제한 2초
가능한 인구 이동은 최대 2000일

1. dfs, bfs 중 어떤 게 더 적절? -> bfs 추천
2. 연합을 어떤 구조로 저장?

dfs로 연합 찾기 -> 연합 어떻게 기록?
연합에 속하는 칸의 좌표를 계속 쌓다가 dfs 끝나면 바로 업데이트
다음 칸으로 이동해서 반복
"""
import sys
sys.setrecursionlimit(10**6)
n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# def dfs(x,y,num,route,total):
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<n and 0<=ny<n and temp[nx][ny] == 0 and l<=abs(countries[x][y]-countries[nx][ny])<=r:
#             temp[nx][ny] = num # 방문 처리
#             route.append((nx,ny))
#             total+=countries[nx][ny]
#             # for t in temp:
#             #     print(*t)
#             dfs(nx,ny,num,route,total)
#     return route, total

def dfs(x,y,num):
    global route, total
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and temp[nx][ny] == 0 and l<=abs(countries[x][y]-countries[nx][ny])<=r:
            temp[nx][ny] = num # 방문 처리
            route.append((nx,ny))
            total+=countries[nx][ny]
            # for t in temp:
            #     print(*t)
            dfs(nx,ny,num)

def update(route, total):
    val = total//len(route)
    for x,y in route:
        countries[x][y] = val

ans = 0
while True:
    num = 0
    con = False
    temp = [[0]*n for _ in range(n)] # 연합 저장
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 0:
                num += 1
                temp[i][j] = num
                route = [(i,j)]
                total = countries[i][j]
                dfs(i,j,num)
                # print(route, total)
                if len(route) > 1:
                    con = True
                    update(route, total)
    # for t in temp:
    #     print(*t)
    # print("==="*10)
    # for c in countries:
    #     print(*c)
    if not con:
        break
    ans += 1
print(ans)


            











