import sys
# N 5~500,000
input = sys.stdin.readline
N = int(input())
# A: 가로, B: 세로 1~1000
A, B = map(int,input().split())
cor = set()
for _ in range(N):
    x,y = map(int,input().split())
    cor.add((x,y))

count = 0
for x,y in cor:
    if (x+A, y) in cor and (x,y+B) in cor and (x+A, y+B) in cor:
        count +=1
print(count)