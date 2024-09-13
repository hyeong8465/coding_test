import sys
input = sys.stdin.readline
count = 1
while True:
    A = list(input().split())
    if A[0] == '0':
        break
    else:
        print(f'Case {count}: Sorting... done!')
        count += 1 