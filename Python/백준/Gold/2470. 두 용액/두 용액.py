import bisect

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_abs = float('inf')
ans = (0, 0)

for i in range(n):
    target = -arr[i]
    # arr[i+1:] 구간에서 이진 탐색 → i보다 큰 인덱스에서만 탐색
    idx = bisect.bisect_left(arr, target, i + 1, n)

    # idx와 idx - 1 모두 체크해보기 (가까운 후보 둘)
    for j in [idx - 1, idx]:
        if i < j < n:
            s = arr[i] + arr[j]
            if abs(s) < min_abs:
                min_abs = abs(s)
                ans = (arr[i], arr[j])

print(*ans)