"""
10:24
그리디

최대 m원을 사용해서 만들 수 있는 가장 큰 방 번호

매 순간 가장 큰 수 사기
숫자를 많이 사기

1. 가능한 많은 숫자를 사기 & 2. 같은 길이의 수라면 더 큰 수 사기
가능한 많은 숫자 사기 -> 가격이 낮은 숫자만 계속 구매 -> 최적해가 아님
[반례]
3
100 7 8
16
11: 14원
22: 16원

각 숫자마다 최대로 구매할 수 있는 갯수를 계산
최대 구매할 수 있는 게 0이면 0의 갯수를 하나씩 줄여가면서 살 수 있는 가장 큰 수
0이 아니면 남은 금액으로 살 수 있는 가장 큰 수 추가

[반례]
3
3 7 8
19




m: 50
n: 10
2초

포기.
인터넷 참고
"""

# n = int(input())
# temp = list(map(int, input().split()))
# prices = []
# for i in range(n):
#     prices.append((i, temp[i]))
# prices.sort(key = lambda x:(x[1], x[0]))
# m = int(input())

# count = [m//t for t in temp]
# print(count)
# max_idx = 0
# max_count = 0
# flag = False
# for i, c in enumerate(count):
#     if c >= max_count:
#         if c == max_count:
#             flag = True
#         max_idx = i
#         max_count = c
        
# print(max_idx, max_count)


n = int(input())
prices = list(map(int, input().split()))
m = int(input())
dp = [-float('inf')] * (m+1)
for i in range(n-1, -1, -1):
    p = prices[i]
    for j in range(p, m+1):
        dp[j] = max(dp[j], i, dp[j-p]*10 + i)
print(dp[m])
