import sys

# 입력 처리
n, k = map(int, sys.stdin.readline().split())
num_str = sys.stdin.readline().rstrip()

# 결과를 담을 스택
stack = []
# 제거 횟수를 저장할 변수
k_removals = k

# 숫자를 하나씩 순회
for digit in num_str:
    # 1. 스택이 비어있지 않고,
    # 2. 아직 지울 횟수가 남았고,
    # 3. 스택의 마지막 숫자가 현재 숫자보다 작으면
    while stack and k_removals > 0 and stack[-1] < digit:
        # 스택에서 마지막 숫자를 제거 (더 큰 숫자로 교체하기 위해)
        stack.pop()
        k_removals -= 1
    
    # 현재 숫자를 스택에 추가
    stack.append(digit)

# 만약 k가 남아있다면(예: "98765" 같은 내림차순 숫자)
# 결과값의 뒤에서부터 k개 만큼 제거
if k_removals > 0:
    result = stack[:-k_removals]
else:
    result = stack
    
# 최종 결과 출력
print("".join(result))