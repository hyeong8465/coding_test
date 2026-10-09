"""
14:42

"""
from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    t_cnt = defaultdict(int)
    for t in tangerine:
        t_cnt[t] += 1
    # print(t_cnt)
    t_cnt_list = [(k, v) for k, v in t_cnt.items()]
    t_cnt_list.sort(key = lambda x: -x[1])
    # print(t_cnt_list)
    temp_k = 0
    for size, num in t_cnt_list:
        if temp_k >= k:
            break
        answer += 1
        temp_k += num
        
    return answer