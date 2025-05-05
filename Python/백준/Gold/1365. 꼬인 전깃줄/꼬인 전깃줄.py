
import bisect
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

res = []
for a in arr:
    idx = bisect.bisect_left(res, a)
    if idx == len(res):
        res.append(a)
    else:
        res[idx] = a
print(n-len(res))