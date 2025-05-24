import bisect

def LIS(arr):
    dp = []
    res = []
    for num in arr:
        idx = bisect.bisect_left(dp,num)
        # print(idx)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
        res.append(idx)
        # print(dp)
    
    return len(dp), res

n = int(input())
arr = list(map(int, input().split()))
ans, res = LIS(arr)
print(ans)
# print(res)

t = ans-1
lis = [-1]*ans
for i in range(n-1, -1, -1):
    if res[i] == t:
        lis[res[i]] = arr[i]
        t -= 1
print(*lis)