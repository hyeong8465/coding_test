"""
1. 1칸 혹은 2칸 이동
2. 3칸 연속 금지

"""

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0]*301
dp[0] = arr[0]
if n == 1:
    print(dp[0])
    quit()
dp[1] = max(arr[0]+arr[1], arr[1])
if n == 2:
    print(dp[1])
    quit()
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])
count = 0
for i in range(3, n):
    dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
print(dp[n-1])
    