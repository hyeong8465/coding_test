

# 선형 탐색
n = int(input())
arr = list(map(int, input().split()))

lis_dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            lis_dp[i] = max(lis_dp[i], lis_dp[j]+1)

lds_dp = [1]*n
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[j] < arr[i]:
            lds_dp[i] = max(lds_dp[i], lds_dp[j]+1)

max_len = 0
for i in range(n):
    current_len = lis_dp[i] + lds_dp[i] - 1
    max_len = max(max_len, current_len)
print(max_len)