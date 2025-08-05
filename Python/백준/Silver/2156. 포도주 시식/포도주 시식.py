n = int(input())

wine = [int(input()) for _ in range(n)]
dp = [0]*n
dp[0] = wine[0]

if n > 1:
    dp[1] = wine[1]+wine[0]

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])
print(max(dp))