import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = input().rstrip()
target = 'I'+'OI'*n
answer = 0
for i in range(len(a)):
    if a[i] == 'I':
        if a[i:i+2*n+1] == target: answer += 1
        
print(answer)