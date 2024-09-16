import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr_cum = []
val = 0
for i in arr:
    val += i
    arr_cum.append(val)
for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(arr_cum[j-1])
    else:
        print(arr_cum[j-1] - arr_cum[i-2])