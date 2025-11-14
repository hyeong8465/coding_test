"""
10:26


1. 맞닿은 톱니의 극이 다르다면, 반대방향으로 회전
2. 맞닿은 톱니의 극이 같으면, 회전하지 않음


구현, 시뮬
"""
from collections import deque

gears = [deque(list(map(int, list(input())))) for _ in range(4) ]
k = int(input())

def move(gear, direction):
    if direction == 1:
        right = gear.pop()
        gear.appendleft(right)
    elif direction == -1:
        left = gear.popleft()
        gear.append(left)

for _ in range(k):
    direction_list = [0]*4
    num, direction = map(int, input().split())
    num = num-1
    
    direction_list[num] = direction
    # 오른쪽에 있는 톱니에 대해서 방향 설정
    idx = num
    while idx < 3:
        if gears[idx][2] == gears[idx+1][6]:
            direction_list[idx+1] = 0
        else:
            direction_list[idx+1] = -direction_list[idx]
        idx+=1
    # 왼쪽에 있는 톱니에 대해서 방향 설정
    
    idx = num
    while idx > 0:
        if gears[idx][6] == gears[idx-1][2]:
            direction_list[idx-1] = 0
        else:
            direction_list[idx-1] = -direction_list[idx]
        idx-=1
    
    # print(direction_list)

    for idx, d in enumerate(direction_list):
        move(gears[idx], d)
    
    # for gear in gears:
        # print(gear)

answer = 0
for i, gear in enumerate(gears):
    answer += gear[0]*2**i
print(answer)
        


    


