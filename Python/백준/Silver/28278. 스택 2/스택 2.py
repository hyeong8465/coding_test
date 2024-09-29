import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    input_str = input().rstrip()
    if input_str[0] == '1':
        a, b = input_str.split()
        stack.append(b)
    
    elif input_str[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop()) 
    elif input_str[0] == '3':
        print(len(stack))
    elif input_str[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])