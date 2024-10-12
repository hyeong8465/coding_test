import sys

input = sys.stdin.readline

x = int(input())
d = [[0,[1]] for _ in range(10**6+1)]
# print(d)
for i in range(2, x+1):
    d[i][0] = d[i-1][0]+1 # 1로 빼는 경우
    d[i][1] = d[i-1][1]+[i] # 경로
    if i % 2 == 0:
        if d[i//2][0]+1 <= d[i][0]:
            d[i][0] = d[i//2][0]+1
            d[i][1] = d[i//2][1]+[i]
    if i % 3 == 0:
        if d[i//3][0]+1 <= d[i][0]:
            d[i][0] = d[i//3][0]+1
            d[i][1] = d[i//3][1]+[i]
print(d[x][0])
d[x][1].reverse()
print(*d[x][1])