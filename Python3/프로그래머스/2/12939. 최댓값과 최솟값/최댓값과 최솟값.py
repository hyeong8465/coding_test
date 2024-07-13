def solution(s):
    s_list = s.split(' ')
    num = [int(i) for i in s_list]
    answer = str(min(num))+' '+str(max(num))
    return answer