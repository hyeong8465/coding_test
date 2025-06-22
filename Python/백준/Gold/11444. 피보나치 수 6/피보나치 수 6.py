import sys

# 입력 n과 나눌 수 MOD 설정
n = int(sys.stdin.readline())
MOD = 1000000007

# 2x2 행렬 곱셈 함수 (이전과 동일)
def mat_mul(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= MOD
    return C

# 2x2 행렬 거듭제곱 함수 (수정된 버전 - 반복문 사용)
def mat_pow(A, k):
    # 결과 행렬을 단위 행렬로 초기화
    # A^0 = I (단위 행렬)
    result = [[1, 0], [0, 1]]
    
    # k가 0보다 클 때까지 반복
    while k > 0:
        # k가 홀수이면, 결과 행렬에 A를 한 번 더 곱해줌
        if k % 2 == 1:
            result = mat_mul(result, A)
        
        # A를 제곱하고, k는 절반으로 줄임
        A = mat_mul(A, A)
        k //= 2
        
    return result

# 메인 로직
if n == 0:
    print(0)
else:
    # 피보나치 기본 행렬
    base_matrix = [[1, 1], [1, 0]]
    
    # F(n)을 구하기 위해 base_matrix를 (n)번 거듭제곱
    # 이전 코드에서는 n-1을 사용했으나, n으로 계산하고
    # 결과 행렬의 [0][1] 원소를 취하는 것이 F(n)에 해당합니다.
    # [F(n+1), F(n)]^T = T^n * [F(1), F(0)]^T
    # T^n * [1, 0]^T 의 결과 벡터에서 2행 1열 성분이 F(n) 입니다.
    if n == 1:
        print(1)
    else:
        result_matrix = mat_pow(base_matrix, n - 1)
        print(result_matrix[0][0])