"""
2:45

"""
n = int(input())
dp = [0]*(n+1)

arr = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    day, cost = arr[i]
    # print(i+day-1)
    dp[i] = max(dp[i-1], dp[i])
    if 0 <= i+day-1 < n:
        # if day == 1:
        #     dp[i] = dp[i]+cost
        # else:
        dp[i+day-1] = max(dp[i+day-1], dp[i-1]+cost)
#    print(dp)
print(max(dp))
 