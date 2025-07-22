"""
15:00
stack
n자리 숫자에서 k개의 숫자를 지워서 얻을 수 있는 가장 큰 수 구하기

k, n: 50만


try1: 완전 탐색
nCk -> 시간 초과

try2: stack
stack의 맨 뒤보다 낮은 값이 오면 스택에 쌓고
더 큰 값이면 맨 뒤를 빼고 넣음

"""
# O(N*K)
n, k = map(int, input().split())
num = input()

result = []

start_index = 0
for i in range(n - k):
    end_index = k + i + 1
    
    max_digit = '0'
    max_idx = start_index
    for j in range(start_index, end_index):
        if num[j] > max_digit:
            max_digit = num[j]
            max_idx = j
            if max_digit == '9':
                break
    
    # 찾은 가장 큰 숫자를 결과에 추가
    result.append(max_digit)
    # 다음 탐색은 찾은 위치 바로 다음부터 시작
    start_index = max_idx + 1

print("".join(result))

# O(N)



