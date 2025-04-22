
from itertools import combinations
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    arr = []
    total_x = 0
    total_y = 0
    for _ in range(n):
        temp = tuple(map(int, input().split()))
        total_x += temp[0]
        total_y += temp[1]
        arr.append(temp)
    # print(total_x, total_y)
    
    cands = list(combinations(arr, n//2))
    result = float('inf')
    for cand in cands:
        start_x = 0
        start_y = 0
        for c in cand:
            start_x+=c[0]
            start_y+=c[1]
        end_x = total_x-start_x
        end_y = total_y-start_y
        dis = ((end_x-start_x)**2 + (end_y-start_y)**2)**0.5
        result = min(result, dis)
    print(result)