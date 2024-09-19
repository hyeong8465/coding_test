import sys
input = sys.stdin.readline

while True:
    char = input().rstrip()
    stack = []
    if char == '.':
        quit()
    plag = 0
    for i in char:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                print('no')
                plag = 1
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                plag = 1
                break
        elif i == '[':
            stack.append('[')
        elif i == ']':
            if len(stack) == 0:
                print('no')
                plag = 1
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                plag = 1
                break
    if plag == 0:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')