import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr = sorted(arr, key = lambda x: (x[1],x[0]))

endtime = arr[0][1]
answer = 1

for i in range(1,n):
    starttime = arr[i][0]
    if starttime < endtime:
        continue
    endtime = arr[i][1]
    answer += 1

print(answer)


    
    
