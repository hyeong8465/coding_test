n = int(input())
arr = list(map(int, input().split()))
nge = [-1]*n
stack = [0] # 원소의 인덱스
# 스택에는 오큰수를 못 찾은 인덱스를 저장

for i in range(1,n):
#    print(stack, nge)
    while stack and arr[stack[-1]] < arr[i]:
        nge[stack.pop()] = arr[i]
    stack.append(i)
print(*nge)