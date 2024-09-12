# Q, D, N, P
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    C = int(input()) # 센트
    Q, D, N, P = 0, 0, 0, 0
    while C >= 25:
        Q += 1
        C -= 25
    while C >= 10:
        D += 1
        C -= 10
    while C >= 5:
        N += 1
        C -= 5
    while C >= 1:
        P += 1
        C -= 1
    print(Q, D, N, P)