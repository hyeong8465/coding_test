def solution(numbers):
    temp = [str(num) for num in numbers]
    temp.sort(key=lambda x: x * 4, reverse=True)
    answer = ''.join(temp)
    return '0' if answer[0] == '0' else answer  # 전부 0이면 맨 앞이 항상 '0'