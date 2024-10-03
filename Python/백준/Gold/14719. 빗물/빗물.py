

import sys
input = sys.stdin.readline

h, w = map(int,input().split())
building = list(map(int, input().split()))
answer = 0
for i in range(h, 0, -1):
    temp = []
    for idx, b in enumerate(building):
        if b >= i:
            temp.append(idx)
    # print(i, temp)
    if len(temp) == 1:
        continue
    else:
        temp_range = [temp[i+1]-temp[i]-1 for i in range(0,len(temp)-1)]
    # print(temp_range)
    answer += sum(temp_range)
print(answer)