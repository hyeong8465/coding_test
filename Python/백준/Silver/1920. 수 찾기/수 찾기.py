import sys
input = sys.stdin.readline

a = input()
temp = list(map(int, input().split()))
dic = {}
for t in temp:
    dic[t] = 1
b = input()
arr = list(map(int, input().split()))
for i in arr:
    if i in dic:
        print(1)
    else:
        print(0)