import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    # 잘라낸 나무 길이 합 계산
    cut_sum = 0
    for t in trees:
        if t >= mid:
            cut_sum += t - mid

    if cut_sum >= M:
        # M 이상이면 톱날을 더 높여도 가능
        result = mid
        start = mid + 1
    else:
        # M 이하이면 톱날을 낮춰야 한다
        end = mid - 1

print(result)