def solution(name):
    n = len(name)
    answer = 0
    for c in name:
        d = ord(c) - 65
        answer += min(d, 26 - d)

    min_move = n - 1  # 기본값: 방향 전환 없이 끝까지 오른쪽으로
    for i, c in enumerate(name):
        next_pos = i + 1
        while next_pos < n and name[next_pos] == 'A':
            next_pos += 1
        move = min(i * 2 + (n - next_pos), (n - next_pos) * 2 + i)
        min_move = min(min_move, move)

    return answer + min_move