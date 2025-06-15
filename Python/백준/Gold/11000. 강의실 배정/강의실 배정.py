import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

heap = []
for start, end in arr:
    if heap and heap[0] <= start:
        heapq.heappop(heap)  # 기존 강의실 사용 가능
    heapq.heappush(heap, end)  # 새로운 수업 할당

print(len(heap))  # 현재 heap에 들어있는 수업 수 == 필요한 강의실 수