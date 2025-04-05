from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
temp = list(map(int, input().split()))

opers = ['add'] * temp[0] + ['sub'] * temp[1] + ['mul'] * temp[2] + ['div'] * temp[3]
combs = set(permutations(opers, n - 1))  # 중복 제거!

answer_min = float('inf')
answer_max = float('-inf')

for comb in combs:
    res = nums[0]
    for idx, op in enumerate(comb):
        if op == 'add':
            res += nums[idx + 1]
        elif op == 'sub':
            res -= nums[idx + 1]
        elif op == 'mul':
            res *= nums[idx + 1]
        elif op == 'div':
            if res < 0:
                res = -(-res // nums[idx + 1])
            else:
                res = res // nums[idx + 1]
    answer_min = min(answer_min, res)
    answer_max = max(answer_max, res)

print(answer_max)
print(answer_min)