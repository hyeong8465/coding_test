import sys
input = sys.stdin.readline

# 입력 받기
n, k = map(int, input().split())  # 물건 개수, 배낭 최대 무게
items = [tuple(map(int, input().split())) for _ in range(n)]  # (무게, 가치)

# DP 배열 선언 (배낭 무게 k까지)
dp = [0] * (k + 1)

# DP 점화식 적용 (배낭 문제는 역순으로 순회)
for w, v in items:
#    print(w,v)
    for j in range(k, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
#        print(dp)

# 최댓값 출력
print(dp[k])