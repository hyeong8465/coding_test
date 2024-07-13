def solution(s):
    s_list = s.split(' ')
    num = [int(i) for i in s_list]
    num.sort()
    answer = ''
    answer += str(num[0])
    answer += ' '
    answer += str(num[-1])
    return answer