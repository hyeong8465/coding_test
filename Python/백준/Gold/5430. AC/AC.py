import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    temp = input().rstrip()[1:-1]  # 대괄호 제거
    
    if temp:
        q = deque(temp.split(','))
    else:
        q = deque()
    
    error = False
    rev = False
    
    for i in p:
        if i == 'R':
            rev = not rev
        elif i == 'D':
            if not q:
                error = True
                break
            if rev:
                q.pop()
            else:
                q.popleft()
    
    if error:
        print('error')
    else:
        if rev:
            q.reverse()
        print('[' + ','.join(q) + ']')