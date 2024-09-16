import sys
input = sys.stdin.readline

a = int(input())
for _ in range(a):
    b, c = input().split()
    b = int(b)
    answer = ''
    for i in c:
        answer += i*b
    print(answer)