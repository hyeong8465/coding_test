import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_heap = []
for _ in range(n):
    temp = int(input())
    if temp == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            val = heapq.heappop(max_heap)
            print(-val)
    else:
        heapq.heappush(max_heap, -temp)