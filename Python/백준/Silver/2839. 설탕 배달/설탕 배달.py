import sys
input = sys.stdin.readline

N = int(input())
count = 0

while True:
    if N % 5 == 0:
        count += N//5
        break
    else:
        N -= 3
        count += 1
    if N < 0:
        print(-1)
        quit()
print(count)