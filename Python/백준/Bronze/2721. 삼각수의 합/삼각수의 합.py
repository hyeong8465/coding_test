import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer = 0
    n = int(input())
    t = 1
    for i in range(1,n+1):
        t += i+1
        answer += i*t
    print(answer)