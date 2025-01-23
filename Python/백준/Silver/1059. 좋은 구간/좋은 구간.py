"""
A~B 사이에 있는 원소가 s에 속하지 않음
n을 포함하는 좋은 구간의 개수
"""
l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()
if n in s:
    print(0)
    quit()

if s[0] > n:
    left = 1
    right = s[0]-1
elif s[-1] == n:
    print(0)
    quit()
elif s[-1] < n:
    left = s[-1]+1
    right = n
else:
    for i in range(l-1):
        if s[i] < n and s[i+1] > n:
            left = s[i] + 1
            right = s[i+1] - 1
            break
# print(left, right)
cnt = (n-left+1) * (right - n+1) - 1
print(cnt)
"""
1 / 2

9, 10, 11, 12
9 10 / 10 11
9 10 11 / 10 11 12
9 10 11 12

"""

