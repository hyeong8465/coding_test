
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
idx = 0

for _ in range(q):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        arr[(idx+temp[1]-1)%n] += temp[2]
    elif temp[0] == 2:
        idx -= temp[1]
    else:
        idx += temp[1]

for i in range(idx, idx+n):
    print(arr[i%n], end=' ')