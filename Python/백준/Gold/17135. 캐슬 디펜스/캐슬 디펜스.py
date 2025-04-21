from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

n, m, d = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
arr = []
enemies = {}
enemies_num = 1
for row in range(n):
    temp = list(map(int, input().split()))
    for col, t in enumerate(temp):
        if t == 1:
            enemies[enemies_num] = (row,col)
            enemies_num += 1
    arr.append(temp)
# print(enemies)

temp = [i for i in range(m)]
pos = list(combinations(temp,3))

# 적 선택
def distance(x,y, enemies):
    temp = []
    for k,v in enemies.items():
        dis = abs(x-v[0])+abs(y-v[1])
        if dis <= d:
            temp.append((dis, k, v[0], v[1]))
    if len(temp) == 0:
        return False
    temp.sort(key = lambda x: (x[0], x[3])) # 가장 가까운 적 and 왼쪽
    return temp[0][1]

answer = 0
# print(pos)
for p in pos:
    arr_temp = copy.copy(arr)
    enemies_temp = copy.copy(enemies)
    result = 0
    for i in range(n+1): # 0번줄부터 n줄까지
        # 삭제할 적 저장
        enemies_del = set()
        for archer in p:
            dis = distance(n, archer, enemies_temp)
            if not dis:
                continue
            else:
                enemies_del.add(dis)
        # print(enemies_del)
        
        # 삭제
        for e in enemies_del:
            del enemies_temp[e]
            result += 1
        
        # print(enemies_temp)
        # 이동
        end = []
        for k,v in enemies_temp.items():
            if v[0]+1 == n:
                end.append(k)
            else:
                enemies_temp[k] = (v[0]+1, v[1])
        for e in end:
            del enemies_temp[e]
    answer = max(result, answer)

print(answer)