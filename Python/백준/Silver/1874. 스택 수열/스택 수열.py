import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
answer = []
current = 1

for num in arr:
    # current가 num에 도달할 때까지 스택에 숫자를 넣습니다.
    while current <= num:
        stack.append(current)
        answer.append('+')
        current += 1
    # 스택의 최상단이 num과 같다면 pop
    if stack and stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit(0)

for op in answer:
    print(op)