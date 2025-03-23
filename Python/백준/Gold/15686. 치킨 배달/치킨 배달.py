"""
14:16
try1: m개 고르는 경우의 수마다 bfs 적용 -> 시간초과

bfs 안해도 되네 그냥 집이랑 치킨집 좌표빼서 절대값으로 거리 계산 가능


"""
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [] # 마을
c_arr = [] # 치킨집 위치
h_arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j, t in enumerate(temp):
        if t == 2:
            c_arr.append((i,j)) # 치킨집 위치 저장
        elif t == 1:
            h_arr.append((i,j)) # 가정집 위치 저장

def distance(cand):
    result = 0
    for hx, hy in h_arr: # 모든 집에 대해서
        temp = 1e9
        for cx,cy in cand:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result

c = list(combinations(c_arr, m))

result = 1e9
for cand in c:
    result = min(result, distance(cand))
print(result)
