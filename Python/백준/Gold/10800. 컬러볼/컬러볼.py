# import sys
# input = sys.stdin.readline

# n = int(input())

# arr = []
# for i in range(n):
#     c, w = map(int, input().split())
#     arr.append((i, c, w))

# arr.sort(key=lambda x: x[2])  # weight 기준만으로 충분

# ans = [0] * n
# color_sum = [0] * (n + 1)
# total = 0

# for idx, c, w in arr:
#     ans[idx] = total - color_sum[c]
#     color_sum[c] += w
#     total += w

# for a in ans:
#     print(a)

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    c, w = map(int, input().split())
    arr.append((i, c, w))

# 무게 오름차순 정렬 (색상 기준 tie-breaker 필요 없습니다)
arr.sort(key=lambda x: x[2])

ans = [0] * n
total = 0
color_sum = [0] * (n + 1)

i = 0
while i < n:
    # 같은 무게 그룹의 시작 인덱스
    start = i
    weight = arr[i][2]
    # 그룹 끝 인덱스 찾기
    while i < n and arr[i][2] == weight:
        i += 1
    end = i  # [start, end) 구간이 같은 weight

    # 1) 그룹 내 각 공의 답 구하기
    for j in range(start, end):
        idx, color, w = arr[j]
        ans[idx] = total - color_sum[color]

    # 2) 그룹 전체를 누적합에 반영
    group_size = end - start
    total += weight * group_size
    for j in range(start, end):
        _, color, _ = arr[j]
        color_sum[color] += weight

# 출력
print('\n'.join(map(str, ans)))