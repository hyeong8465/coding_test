
"""
시작 11:35

n개의 카드

카드 섞는 순서가 있는 수열 S
카드가 분배되는 수열 P
"""

n = int(input())


p = list(map(int, input().split()))
s = list(map(int, input().split()))

init = p[:]
ans = 0
while [0,1,2]*(n//3) != p:
    temp = [0]*n
    for i in range(n):
        temp[s[i]] = p[i]
    if init == temp:
        ans = -1
        break
    ans += 1
    p = temp
print(ans)

