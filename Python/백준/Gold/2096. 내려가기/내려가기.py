import sys
input = sys.stdin.readline

n = int(input())
first_row = list(map(int, input().split()))

max_dp = first_row[:]  # 최댓값 DP 배열
min_dp = first_row[:]  # 최솟값 DP 배열

for _ in range(n-1):
    a, b, c = map(int, input().split())

    # 최대값 업데이트 (이전 값 사용)
    new_max_dp = [
        a + max(max_dp[0], max_dp[1]),
        b + max(max_dp[0], max_dp[1], max_dp[2]),
        c + max(max_dp[1], max_dp[2])
    ]

    # 최소값 업데이트 (이전 값 사용)
    new_min_dp = [
        a + min(min_dp[0], min_dp[1]),
        b + min(min_dp[0], min_dp[1], min_dp[2]),
        c + min(min_dp[1], min_dp[2])
    ]

    # 값 업데이트 (슬라이딩 윈도우 방식)
    max_dp = new_max_dp
    min_dp = new_min_dp

# 최댓값과 최솟값 출력
print(max(max_dp), min(min_dp))