def solution(number, k):
    stack = []
    cnt = 0
    for i in range(len(number)):
        while stack:
            if number[i] <= stack[-1]:
                stack.append(number[i])
                break
            stack.pop()
            cnt += 1
            if cnt == k:
                return ''.join(stack)+number[i:]
        else:
            stack.append(number[i])
    
    
    return ''.join(stack[:len(number)-k])