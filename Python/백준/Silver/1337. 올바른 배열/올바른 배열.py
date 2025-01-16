
n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()
min_additions = 5  # 최대 5개의 수가 필요할 수 있으므로 초기값을 5로 설정

for i in range(n):
    for j in range(i, n):
        if arr[j] - arr[i] < 5:
            current_length = j - i + 1
            additions_needed = 5 - current_length
            min_additions = min(min_additions, additions_needed)
        else:
            break

print(min_additions)