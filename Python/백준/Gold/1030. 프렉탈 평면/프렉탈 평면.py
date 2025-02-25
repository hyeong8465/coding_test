def is_black(s, n, k, r, c):
    if s == 0:
        return 0  # 기본적으로 0으로 시작

    block_size = n ** (s - 1)  # 현재 단계에서 한 블록의 크기
    center_start = (n - k) // 2 * block_size  # 중앙 영역 시작
    center_end = center_start + k * block_size - 1  # 중앙 영역 끝

    # 현재 위치가 중앙 검은색 영역에 속하면 1
    if center_start <= r <= center_end and center_start <= c <= center_end:
        return 1
    
    # 아니라면 더 작은 블록에서 확인
    return is_black(s - 1, n, k, r % block_size, c % block_size)

# 입력
s, n, k, r1, r2, c1, c2 = map(int, input().split())

# 출력할 범위 계산
for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        print(is_black(s, n, k, r, c), end="")
    print()