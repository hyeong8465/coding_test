"""
10:53
수업 n개
최소의 강의실 사

n: 20만
flatten해서 시작, 종료
현재 사용중인 강의실 수만 체크
"""
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s,t = map(int, input().split())
    arr.append((s,0))
    arr.append((t,1))
arr.sort(key = lambda x: (x[0],-x[1]))

# print(arr)

ans = 0
temp = 0
for time, state in arr:
    if state == 0:
        temp += 1
        ans = max(ans, temp)
    else:
        temp -= 1
    # print(ans)
print(ans)
    

