import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n  # 최소 길이는 자기 자신 하나

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:  # 증가하는 부분 수열 조건
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # 가장 긴 LIS 길이 출력