"""
인접한 집의 색은 달라야 함
1은 2, n이랑 겹치면 안됨
"""
import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
INF = 1e9
answer = []
for c in [0,1,2]:
    dp = [INF, INF, INF]
    dp[c] = cost[0][c]

    for i in range(1,n):
        new_dp = [
            min(dp[1]+cost[i][0], dp[2]+cost[i][0]),
            min(dp[0]+cost[i][1], dp[2]+cost[i][1]),
            min(dp[0]+cost[i][2], dp[1]+cost[i][2])
        ]
        dp = new_dp
        # print(cost[i], dp)
    dp[c] = INF
    answer.append(min(dp))
print(min(answer))