import sys
input = sys.stdin.readline

n = int(input())
que = []
for _ in range(n):
    temp = list(input().rstrip().split())
    if temp[0] == 'push':
        que.append(int(temp[1]))
    elif temp[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            del que[0]
    elif temp[0] == 'size':
        print(len(que))
    elif temp[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif temp[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])