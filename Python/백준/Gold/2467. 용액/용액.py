"""
산성: 1~10억
알칼리: -10억~-1

두 용액을 합하여 값이 0에 가까운 용액 만들기

"""
import bisect

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = float('inf')
ans = []
# print(arr)
for i in range(n):
    val = -arr[i]
    # arr[i+1:] 범위에서 탐색 
    idx = bisect.bisect_left(arr, val, i+1, n)
    # print(111, idx)
    # if idx == n:
    #     idx -= 1
    # print(222, idx)
    for j in [idx-1, idx]:
        if i<j<n:
            idx = j
            if result > abs(arr[i]+arr[idx]):
                result = abs(arr[i] + arr[idx])
                ans = [arr[i], arr[idx]]

print(*ans)