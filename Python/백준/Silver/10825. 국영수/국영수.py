import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    temp = input().rstrip().split()
    # print(temp)
    arr.append([temp[0],int(temp[1]), int(temp[2]), int(temp[3])])

# print(arr)
arr.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))

for i in arr:
    print(i[0])
    
    
    