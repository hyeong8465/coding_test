import sys

input = sys.stdin.readline


def max_n(inner_idx):
    tmp, idx = a[inner_idx], inner_idx
    for i in range(inner_idx + 1, min(n, inner_idx + s + 1)):
        if a[i] > tmp:
            tmp = a[i]
            idx = i
    return tmp, idx


n = int(input())
a = list(map(int, input().split()))
s = int(input())
for i in range(n - 1):
    max_Num, max_Idx = max_n(i)
    if max_Idx != i:
        del a[max_Idx]
        a.insert(i, max_Num)
        s -= (max_Idx - i)
print(*a)