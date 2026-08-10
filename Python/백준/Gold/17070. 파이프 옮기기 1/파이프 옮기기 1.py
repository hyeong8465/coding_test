n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# dp[x][y][dir] => (x, y)에 도달했을 때 dir 상태로 오는 경로 수
# dir: 0=가로, 1=세로, 2=대각
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

# 시작 위치: (0,1)에 가로로 있음
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            continue
        # 가로
        if j >= 1:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2] # 가로에서 온거 + 대각에서 온거
        # 세로
        if i >= 1:
            dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        # 대각선
        if i >= 1 and j >= 1:
            if graph[i-1][j] == 0 and graph[i][j-1] == 0:
                dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

# 정답은 (n-1,n-1)에 도달한 모든 상태의 합
print(sum(dp[n-1][n-1]))