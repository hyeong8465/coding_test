import sys
input = sys.stdin.readline

n = int(input())


for _ in range(n):
    x = int(input())
    answer = [0]*(x+1)
    if x == 1:
        print(1)
    elif x == 2:
        print(2)
    elif x == 3:
        print(4)
    else:
        answer[1] = 1
        answer[2] = 2
        answer[3] = 4
        for i in range(4, x+1):
            answer[i] = answer[i-3]+answer[i-2]+answer[i-1]
        print(answer[x])