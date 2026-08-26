from itertools import permutations

def solution(numbers):
    limit = int('9' * len(numbers))
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False

    answer = set()
    for i in range(1, len(numbers)+1):
        for comb in permutations(numbers, i):
            val = int("".join(comb))
            if is_prime[val]:
                answer.add(val)
    return len(answer)