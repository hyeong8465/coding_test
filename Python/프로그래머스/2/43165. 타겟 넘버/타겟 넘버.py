from collections import defaultdict

def solution(numbers, target):
    dp = defaultdict(int)
    dp[0] = 1
    for num in numbers:
        next_dp = defaultdict(int)
        for total, cnt in dp.items():
            next_dp[total + num] += cnt
            next_dp[total - num] += cnt
        dp = next_dp
    return dp[target]