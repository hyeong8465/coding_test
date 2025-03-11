from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = list(permutations(arr, m))
a = list(set(a))
a.sort()
for i in a:
    print(*i)

