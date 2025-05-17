import sys
input = sys.stdin.readline

N = int(input())
MAX = 500  # 문제에서 c,d ≤ 500 이 보장됨
grid = [[False] * (MAX+1) for _ in range(MAX+1)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    # 직사각형 내부 (a ≤ x < c, b ≤ y < d) 를 True로 표시
    for x in range(a, c):
        for y in range(b, d):
            grid[x][y] = True

# 덮인 칸의 개수 = 전체 면적
area = 0
for row in grid:
    area += sum(row)
print(area)