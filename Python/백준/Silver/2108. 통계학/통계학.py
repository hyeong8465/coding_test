import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
# print(arr)
length = len(arr)
# mean
print(int(round(sum(arr)/length,0)))
# median
idx = length//2
print(arr[idx])
# mode
freq = {}
for i in set(arr):
    freq[i] = 0
for i in arr:
    freq[i] += 1
mode_val = max(freq.values())
temp = []
for i, j in freq.items():
    if j == mode_val:
        temp.append(i)
temp.sort()
if len(temp) >= 2:
    print(temp[1])
else:
    print(temp[0])

# range
print(arr[-1] - arr[0])