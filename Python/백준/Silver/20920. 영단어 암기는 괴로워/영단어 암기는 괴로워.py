import sys
input = sys.stdin.readline

n ,m = map(int, input().split())
word = {}
for _ in range(n):
    temp = input().rstrip()
    if len(temp) >= m:
        if temp in word:
            word[temp] += 1
        else:
            word[temp] = 1
# print(word)
arr = []
for i, j in word.items():
    arr.append([i,j,len(i)])
arr.sort(key = lambda x: x[0])    
arr.sort(reverse = True, key = lambda x: (x[1],x[2]))
for a in arr:
    print(a[0])