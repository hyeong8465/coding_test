n = int(input())

while n % 2 == 0 and n > 1:
    n //= 2

if n == 1:
    print(1)
else:
    print(0)