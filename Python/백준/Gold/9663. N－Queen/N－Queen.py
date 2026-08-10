n = int(input())
count = 0

cols = set()       # 같은 열에 퀸이 있는지
diag1 = set()      # 같은 ↘ 대각선 (row + col)
diag2 = set()      # 같은 ↙ 대각선 (row - col)

def dfs(row):
    global count
    if row == n:
        count += 1
        return

    for col in range(n):
        if col in cols or (row + col) in diag1 or (row - col) in diag2:
            continue

        cols.add(col)
        diag1.add(row + col)
        diag2.add(row - col)

        dfs(row + 1)

        cols.remove(col)
        diag1.remove(row + col)
        diag2.remove(row - col)

dfs(0)
print(count)