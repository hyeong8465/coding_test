def solution(n, results):
    reach = [[False] * (n + 1) for _ in range(n + 1)]
    for win, lose in results:
        reach[win][lose] = True

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if not reach[i][k]:
                continue
            for j in range(1, n + 1):
                if reach[k][j]:
                    reach[i][j] = True

    answer = 0
    for i in range(1, n + 1):
        known = sum(1 for j in range(1, n + 1) if j != i and (reach[i][j] or reach[j][i]))
        if known == n - 1:
            answer += 1
    return answer