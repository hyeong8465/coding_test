import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a, b = input().rstrip().split()
    arr.append([int(a), b])
arr.sort(key = lambda x: x[0])

for a in arr:
    print(a[0], a[1])