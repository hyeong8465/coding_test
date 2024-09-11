import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
subsets = [[]]
for num in arr:
  size = len(subsets)
  for y in range(size):
    subsets.append(subsets[y]+[num])
    if sum(subsets[y]+[num]) == S:
       count += 1
print(count)