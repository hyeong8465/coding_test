import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 첫 행 읽어서, 왼→오 누적합을 prev[ ]에 저장
first_row = list(map(int, input().split()))

prev = [0]*m
prev[0] = first_row[0]
for j in range(1, m):
    prev[j] = prev[j-1] + first_row[j]

# 두 번째 행부터 마지막 행까지
for _ in range(1, n):
    row = list(map(int, input().split()))

    # 왼쪽→오른쪽 스윕: left_to_right[j] = max(prev[j], left_to_right[j-1]) + row[j]
    left_to_right = [0]*m
    left_to_right[0] = prev[0] + row[0]
    for j in range(1, m):
        left_to_right[j] = max(prev[j], left_to_right[j-1]) + row[j]

    # 오른쪽→왼쪽 스윕: right_to_left[j] = max(prev[j], right_to_left[j+1]) + row[j]
    right_to_left = [0]*m
    right_to_left[m-1] = prev[m-1] + row[m-1]
    for j in range(m-2, -1, -1):
        right_to_left[j] = max(prev[j], right_to_left[j+1]) + row[j]

    # 현재 행의 최댓값은 두 스윕 중 더 큰 값을 취함
    curr = [max(left_to_right[j], right_to_left[j]) for j in range(m)]

    # 이번 행(curr)을 다음 행 계산을 위한 prev로 덮어쓰기
    prev = curr

# 마지막 행의 맨 오른쪽 값이 최종 정답
print(prev[m-1])