import sys

S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())

# T->S
while(1):
    if T == S:
        print(1)
        break
    if len(T) == 0:
        print(0)
        break
    if T[-1] == 'B':
        T.pop()
        T = T[::-1]
    else:
        T.pop()