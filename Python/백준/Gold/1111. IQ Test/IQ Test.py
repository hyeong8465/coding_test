def find_next_number(sequence):
    n = len(sequence)
    
    if n == 1:
        return 'A'
    
    if n == 2:
        if sequence[0] == sequence[1]:
            return sequence[0]
        else:
            return 'A'
    
    x1, x2, x3 = sequence[0], sequence[1], sequence[2]
    
    if x2 - x1 == 0:
        a = 0
    else:
        if (x3 - x2) % (x2 - x1) != 0:
            return 'B'
        a = (x3 - x2) // (x2 - x1)
    
    b = x2 - a * x1
    
    for i in range(1, n):
        if sequence[i] != a * sequence[i - 1] + b:
            return 'B'
    
    return a * sequence[-1] + b

asfd = int(input())
sequence = list(map(int, input().split()))

print(find_next_number(sequence))  # 출력: 6