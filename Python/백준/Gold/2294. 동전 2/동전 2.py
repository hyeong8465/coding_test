import sys
input = sys.stdin.readline

n, price = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [10001] * (price+1)
dp[0] = 0
for i in range(1, price+1):
    for c in coins:
        if i >= c and dp[i-c] != 10001:
            dp[i] = min(dp[i], dp[i-c]+1)
if dp[price] == 10001:
    print(-1)
else:
    print(dp[price])