import sys

input = sys.stdin.readline

n = int(input())  # 탑의 개수
tops = list(map(int, input().split()))  # 탑의 높이
answer = [0] * n  # 결과 배열, 모든 탑은 처음에 0으로 초기화
stack = []  # 탑의 인덱스를 저장할 스택

for i in range(n):
    while stack and tops[stack[-1]] < tops[i]:
        stack.pop()  # 스택의 마지막 탑이 현재 탑보다 작으면 스택에서 제거
    if stack:  # 스택에 남아있는 경우, 더 큰 탑이 존재
        answer[i] = stack[-1] + 1  # 1-based index로 더 큰 탑의 번호 저장
    stack.append(i)  # 현재 탑의 인덱스를 스택에 저장

print(' '.join(map(str, answer)))