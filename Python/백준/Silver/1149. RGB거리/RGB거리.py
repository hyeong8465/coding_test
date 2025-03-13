"""
인접한 집의 색은 달라야 함
dp?
내려가기랑 비슷?
"""
import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = cost[0][:]

for i in range(1,n):
    new_dp = [
        min(dp[1]+cost[i][0], dp[2]+cost[i][0]),
        min(dp[0]+cost[i][1], dp[2]+cost[i][1]),
        min(dp[0]+cost[i][2], dp[1]+cost[i][2])
    ]
    dp = new_dp
    # print(cost[i], dp)
print(min(dp))