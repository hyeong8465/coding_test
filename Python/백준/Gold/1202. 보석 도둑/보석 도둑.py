import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
gems = [list(map(int, input().rstrip().split())) for _ in range(n)]
gems.sort(key = lambda x: -x[0]) # 무게 내림차순

bags = [int(input()) for _ in range(k)]
bags.sort() # 무게 오름차순

ans = 0
cands = []
for bag in bags:
    while gems and gems[-1][0] <= bag:
        m, v = gems.pop()
        heapq.heappush(cands, -v)
    if cands:
        ans += -heapq.heappop(cands)

print(ans)