# bisect
import bisect

n = int(input())
arr = list(map(int, input().split()))

lis_dp = [1]*n
lis = []
for i in range(n):
    idx = bisect.bisect_left(lis, arr[i])
    if idx == len(lis):
        lis.append(arr[i])
    else:
        lis[idx] = arr[i]
    lis_dp[i] = idx + 1

lds_dp = [1]*n
lds = []
for i in range(n-1, -1, -1):
    idx = bisect.bisect_left(lds, arr[i])
    if idx == len(lds):
        lds.append(arr[i])
    else:
        lds[idx] = arr[i]
    lds_dp[i] = idx + 1

max_len = 0
for i in range(n):
    current_len = lis_dp[i] + lds_dp[i] - 1
    if max_len < current_len:
        max_len = current_len

print(max_len)