"""
16:24
문자열정렬

1. 단순 사전식 정렬은 안됨
3 30 34 5 9

9 5 34 30 3
9 5 34 3 30

3433230
3 30 34
4,x,0 -> x의 기준은 앞자리수 -> 어떻게 구현?
"""
from functools import cmp_to_key

def compare(a,b):
    if a+b > b+a:
        return -1
    elif a+b<b+a:
        return 1
    else:
        return 0

def solution(numbers):
    temp = [str(num) for num in numbers]
    temp.sort(key = cmp_to_key(compare))
    answer = ''.join(temp)
    nanswer = None
    for i in range(len(answer)):
        if answer[i] != "0":
            nanswer = answer[i:]
            break
    if nanswer == None:
        nanswer = "0"
    
    return nanswer