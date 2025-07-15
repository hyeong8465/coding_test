import sys
import bisect

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

# 1. 왼쪽 -> 오른쪽으로, 각 원소에서 끝나는 LIS 길이 계산
lis_dp = [0] * n
tails = []
for i in range(n):
    idx = bisect.bisect_left(tails, arr[i])
    if idx == len(tails):
        tails.append(arr[i])
    else:
        tails[idx] = arr[i]
    lis_dp[i] = idx + 1

# 2. 오른쪽 -> 왼쪽으로, 각 원소에서 시작하는 LDS 길이 계산
lds_dp = [0] * n
tails = []
for i in range(n - 1, -1, -1):
    idx = bisect.bisect_left(tails, arr[i])
    if idx == len(tails):
        tails.append(arr[i])
    else:
        tails[idx] = arr[i]
    lds_dp[i] = idx + 1

# 3. LIS와 LDS 길이를 합쳐서 최댓값 찾기
max_len = 0
for i in range(n):
    # 각 i를 "산의 정상"으로 봤을 때의 바이토닉 수열 길이
    current_len = lis_dp[i] + lds_dp[i] - 1
    if max_len < current_len:
        max_len = current_len

print(max_len)