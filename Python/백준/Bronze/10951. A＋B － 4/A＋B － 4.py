
import sys
input = sys.stdin.readline

while True:
    try:
        A, B = map(int, input().split())
        if not A:
            break
        print(A+B)
    except:
        break
            
    