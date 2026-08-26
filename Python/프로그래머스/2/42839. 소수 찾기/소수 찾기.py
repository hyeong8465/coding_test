"""
14:46

1. 숫자 만들기 -> O(8!) -> 대략 4만건  dfs로 생성
2. 소수 판별

"""
from itertools import permutations

def check_prime(value):
    if value in (0,1):
        return False
    if value in (2,3):
        return True
    for val in range(2, int(value**0.5)+1):
        if value%val == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        for comb in permutations(numbers, i):
            val = int("".join(comb))
            if check_prime(val):
                answer.add(val)
    print(answer)
    return len(answer)
