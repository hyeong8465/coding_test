n = int(input())
homes = list(map(int, input().split()))

homes.sort()
if n % 2 == 0:

    print(homes[n//2-1])
else:
    print(homes[n//2])

"""

1 3 6 7



"""