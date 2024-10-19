"""
한번 입었던 조합으로는 입지 않음
다른 요소가 추가되거나 다른 요소로 바꿔야함
"""
import sys
from itertools import *
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    dic = {}
    num = 0
    for _ in range(n):
        a, b = input().rstrip().split()
        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1
            num += 1
    # print(dic)
    ans = 1
    for count in dic.values():
        ans *= (count + 1)  # 해당 종류의 옷을 안 입는 경우를 더해줌
    
    print(ans - 1)  # 아무것도 입지 않는 경우를 제외