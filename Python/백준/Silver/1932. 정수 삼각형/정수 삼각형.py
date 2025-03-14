n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        dp = arr
    else:
        new_dp = [0]*len(arr)
        for i in range(len(arr)):
            if i == 0:
                new_dp[i] = dp[i]+arr[i]
                # print(new_dp)
            elif i == len(arr)-1:
                new_dp[i] = dp[i-1]+arr[i]
            else:
                # print(2)
                new_dp[i] = max(dp[i-1], dp[i])+arr[i]
        dp = new_dp[:]
    # print(dp)
print(max(dp))