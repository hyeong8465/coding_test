import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 원본 배열 입력
A = [ [0]*(n+1) ]
for _ in range(n):
    A.append( [0] + list(map(int, input().split())) )

# 2차원 누적 합 배열 생성
S = [ [0]*(n+1) for _ in range(n+1) ]

for i in range(1, n+1):
    for j in range(1, n+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i][j]

# 쿼리 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(result)