"""
16:42
순서를 바꾸지 않고 +/-만 수정한다.

브루트포스: O(2^20*20) = 2천만 -> 1초
"""
def dfs(numbers, depth, target, operator, now):
    temp_val = now+operator*numbers[depth]
    if depth == len(numbers)-1:
        if temp_val == target:
            return 1
        else:
            return 0
    ans = 0
    for op in [-1,1]:
        ans += dfs(numbers, depth+1, target, op, temp_val)
    return ans

def solution(numbers, target):
    answer = 0
    for op in [-1,1]:
        answer += dfs(numbers, 0, target, op, 0)
    return answer