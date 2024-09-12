import sys

input = sys.stdin.readline

board = input().rstrip()
result = []
count = 0
for char in board:
    if char == 'X':
        count += 1
    elif char == '.':
        if count > 0:
            result.append(count)
            count = 0
        result.append(0)
if count > 0:
    result.append(count)
answer = ''
for length in result:
    if length % 2 == 1:
        print(-1)
        quit()
    elif length == 0:
        answer += '.'
    else:
        while length >= 4:
            answer += 'AAAA'
            length -= 4
        while length >= 2:
            answer += 'BB'
            length -= 2
        
print(answer)