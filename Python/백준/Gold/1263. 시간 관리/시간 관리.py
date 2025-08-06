"""
22:41
정렬

걸리는 시간, 끝내야 할 시간
최대한 늦게 일을 시작할 수 있는 시간은?

n: 1000
t: 1000
s: 1백만

2 3 4 5
      5 6 7 8 9 10 11 12 13
                         13 14
                            14 15 16 17 18 19

작업을 한줄로 만들고 
"""

# n = int(input())
# tasks = [list(map(int, input().split())) for _ in range(n)]

# tasks.sort(key = lambda x: x[1])

# now = 0
# flag = False
# while True:
#     start = now
#     for time, end in tasks:
#         if start+time > end:
#             flag = True
#             break
#         start += time
#     if flag:
#         print(now-1)
#         break
#     now += 1


import sys

input = sys.stdin.readline
n = int(input())
tasks = [list(map(int, input().split())) for _ in range(n)]

tasks.sort(key=lambda x: -x[1])

latest_time = tasks[0][1] 

for time, end in tasks:
    if latest_time > end:
        latest_time = end
    latest_time -= time
if latest_time < 0:
    print(-1)
else:
    print(latest_time)