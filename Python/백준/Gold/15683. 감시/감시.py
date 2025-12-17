"""
21:38
nxm
cctv k개, 종류 5개, 회전 가능
감시하는 방향에 있는 칸 전체 감시 가능, 벽 통과 불과, cctv는 통과 가능
사각 지대의 최소 크기를 구하는 프로그램

시뮬, 완탐

4**8
2**16
모든 cctv에 대해서 방향을 돌려 가면서 사각 지대 카운트, 경우의 수(65,536) -> 최적화할 수 있지 않을까?

함수 1: 방향, 종류를 입력받아서 해당 경로에 # 처리
"""
n, m = map(int,input().split())
office = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

mode = [
    [],
    [[0], [1], [2], [3]], 
    [[0, 2], [1, 3]], 
    [[0, 1], [1, 2], [2, 3], [3, 0]], 
    [[0, 1, 3], [0, 1, 2], [1, 2, 3], [2, 3, 0]], 
    [[0, 1, 2, 3]]
]

cctvs = []
for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <=5:
            cctvs.append((i, j, office[i][j]))

ans = 100
def dfs(index, current_board):
    global ans
    
    if index == len(cctvs):
        ans_cand = 0
        for i in range(n):
            for j in range(m):
                if current_board[i][j] == 0:
                    ans_cand += 1
        ans = min(ans, ans_cand)
        return
    
    x, y, type = cctvs[index]
    # print(x,y,type)
    for dirs in mode[type]:
        copied = [temp[:] for temp in current_board]
        
        # # 채우기
        for d in dirs:
            nx, ny = x, y
            while 0<=nx<n and 0<=ny<m and copied[nx][ny] != 6:
                copied[nx][ny] = "#"

                nx += dx[d]
                ny += dy[d]

        dfs(index+1, copied)
dfs(0,office)
print(ans)



        
