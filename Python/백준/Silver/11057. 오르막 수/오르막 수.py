import sys

input = sys.stdin.readline

n = int(input())
arr = list(range(10,0,-1))

if n == 1:
    print(10)
    quit()
for i in range(n-1):
    for j in range(10):
        arr[j] = sum(arr[j:])
        # print(arr)
    # print(arr)
print(arr[0]%10007)