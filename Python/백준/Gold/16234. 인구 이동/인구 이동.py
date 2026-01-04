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

# global 변수를 안 쓴 버전
def dfs(x,y,num, route):
    route.append((x,y))
    current_total = countries[x][y]
    temp[x][y] = num
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and temp[nx][ny] == 0 and l<=abs(countries[x][y]-countries[nx][ny])<=r:
            child_total = dfs(nx,ny,num, route)
            current_total += child_total
    
    return current_total

# global 변수를 쓴 버전
# def dfs(x,y,num):
#     global route, total
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<n and 0<=ny<n and temp[nx][ny] == 0 and l<=abs(countries[x][y]-countries[nx][ny])<=r:
#             temp[nx][ny] = num # 방문 처리
#             route.append((nx,ny))
#             total+=countries[nx][ny]
#             # for t in temp:
#             #     print(*t)
#             dfs(nx,ny,num)

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
                num+=1
                route = []
                total = dfs(i,j,num, route)
                if len(route) > 1:
                    con = True
                    update(route, total)
    if not con:
        break
    ans += 1
print(ans)

"""
Study
1. 연합을 찾는 과정에서 dfs/bfs 선택?


2. global 변수를 쓰지 않고 route, total 넘기는 법
재귀 함수 안에서
list.append()를 하면 원본 리스트가 수정되기 때문에 재귀 호출이 끝나도 데이터가 남아있음
total += 를 하면 기존 total 값을 바꾸는 게 아니라 새로운 값을 가진 total 변수가 생성됨
-> integer는 immutable 객체이기 때문에 total 값을 아무리 수정해도 부모 함수에 있는 total 변수에 아무런 영향을 주지 않음

자식 함수가 return하고, 부모함수에서 해당 값을 extend, += 하면 됨
하지만 매번 extend하는 건 느리기 때문에, 리스트는 인자로 넘기고 합계는 리턴받는 방식 추천


3. bfs로 구현



"""
            











