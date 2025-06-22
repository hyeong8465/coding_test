import sys

A, B, C = map(int, sys.stdin.readline().split())

def power_iterative(a, b, c):
    result = 1
    a = a % c
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        
        b //= 2
        
    return result

print(power_iterative(A, B, C))