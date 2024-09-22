import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(input().rstrip())

val = 0
answer = 0
for size in range(min(n,m)):
    for r in range(n-size):
        for c in range(m-size):
            if int(arr[r][c]) == int(arr[r+size][c]) and int(arr[r][c]) == int(arr[r][c+size]) and int(arr[r][c]) == int(arr[r+size][c+size]):
                answer = (size+1)**2

print(answer)