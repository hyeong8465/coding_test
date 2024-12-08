import sys
import heapq
input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    val = int(input())
    if val == 0:
        if len(h) == 0:
            print(0)
        else:
            temp = heapq.heappop(h)
            print(temp)
    else:
        heapq.heappush(h, val)