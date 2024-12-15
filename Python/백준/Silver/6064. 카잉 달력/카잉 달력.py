import sys
input = sys.stdin.readline

cnt = int(input())
arr = [list(map(int, input().split())) for _ in range(cnt)]
for i in arr:
    m, n, t_x,t_y = i
    i = 0
    year = t_x
    pos = False
    while year <= m*n:
        if (year-t_x)%m ==0 and (year-t_y)%n == 0:
            pos = True
            print(year)
            break
        year+=m
    if not pos:
        print(-1)