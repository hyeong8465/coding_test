import heapq
import sys
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)

result = 0
if n == 1:
    print(0)
    quit()
while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += a+b
    heapq.heappush(cards, a+b)
print(result)