
# 이분 탐색 LIS
import bisect

def LIS(arr):
    dp = []
    for num in arr:
        idx = bisect.bisect_left(dp,num)
        # print(idx)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
        # print(dp)
    return len(dp)

n = int(input())
arr = list(map(int, input().split()))
print(LIS(arr))