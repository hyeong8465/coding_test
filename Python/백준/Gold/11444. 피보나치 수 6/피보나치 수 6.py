"""
14:10

try 1
dp: O(N) 불가능, 시간 & 메모리 모두 터짐
n: 10^19

try 2
거듭제곱 분할정복
"""
n = int(input())
MOD = 1000000007

def mat_mul(a, b):
    c = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k]*b[k][j]
            c[i][j] %= MOD
    return c

def mat_pow(a, k):
    result = [[1,0], [0,1]]

    while k > 0:
        if k%2 == 1:
            result = mat_mul(result, a)
        a = mat_mul(a,a)
        k //= 2

    return result

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    base = [[1,1], [1,0]]

    result = mat_pow(base, n-1)

    print(result[0][0])
