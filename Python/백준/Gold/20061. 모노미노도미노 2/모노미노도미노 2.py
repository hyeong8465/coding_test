"""
11:50

블록: 1x1, 1x2, 2x1

1. 빨간색 보드 블록을 둠
    1. 초록색 블록은 상에서 하로(row 증가)
    2. 파란색 블록은 좌에서 우로(col 증가)

2. 초록색 보드에 어떤 행이 타일로 가득차 있으면 해당 행의 타일은 모두 사라짐
    사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동
3. 파란색 보드에 어떤 열이 타일로 가득차 있으면 해당 열의 타일이 모두 사라짐
    사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동
4. 사라지는 행과 열의 갯수만큼 점수 획득

5. 초록색의 0,1행과 파란색의 0,1열은 특별한 칸
    1. 초록색 보드의 0,1행에 블록이 있으면 블록이 있는 행의 수만큼 아래 행에 있는 타일 삭제
    2. 파란색 보드의 0,1열에 블록이 있으면 블록이 있는 열의 수만큼 아래 행에 있는 타일 삭제

행이나 열이 가득찬 경우와 특수 칸에 블록이 있는 경우가 동시에 발생하면,
    행이나 열이 타일로 가득찬 경우가 없을 때까지 점수 획득 후, 특수 칸 처리

얻은 점수와 타일이 있는 칸의 수?

구현, 시뮬
시간복잡도: O(N*6*4)?

파랑과 초록은 일종의 대칭관계
green: 6x4
blue: 6x4
    input (1,1)
    green (0,1)
    blue (0,1)

    input (3,0), (3,1) -> row는 상관없음
    green (0,0), (0,1)
    blue (0,3), (1,3) -> input의 row를 col

    input (2, 2), (3, 2) / (2, 3), (3, 3)
    green (0,2), (1,2) / (0,3), (1,3)
    blue (0,2), (0,3)

1. 입력 데이터 green과 blue의 특수 칸에 둠
green: (input의 row%2, input의 col) 
blue: (input의 col%2, input의 row)

2. 이동
def move: 아래로 내리는 함수

3. 도착한 곳의 row가 가득 찼는지 확인 및 삭제
def check1(row):
    if sum(row) == 4:
        arr.pop(row)
        arr.appendleft(row)

4. 특수 칸에 블록이 있는지 확인
def check2()
    if 블록이 있음
        블록이 있는 row의 수만큼 arr.pop()
        arr.appendleft([0]*4)
"""
from collections import deque
import sys
input = sys.stdin.readline

def move(color, blocks_for_color):
    plag = True
    temp = blocks_for_color

    while plag:
        ntemp = []
        for i, j in temp:
            if i>= 5 or color[i+1][j] == 1:
                plag = False
                break
            ntemp.append((i+1,j))
        if plag:
            temp = ntemp

    for i, j in temp:
        color[i][j] = 1

def check_and_delete(color):
    idx = []
    
    for i in range(2,6):
        if sum(color[i]) == 4:
            idx.append(i)
    
    for i in reversed(idx):
        del color[i]
    
    for _ in range(len(idx)):
        color.appendleft([0]*4)
    
    return len(idx)

def check_special_row(color):
    cnt = 0
    for i in range(0,2):
        if sum(color[i]) != 0:
            cnt += 1
    
    for _ in range(cnt):
        color.pop()
        color.appendleft([0]*4)


n = int(input())
orders = [list(map(int, input().split())) for _ in range(n)]
green = deque([deque([0]*4) for _ in range(6)])
blue = deque([deque([0]*4) for _ in range(6)])

ans = 0
for t, x, y in orders:
    if t == 1:
        blocks_for_green = [(0, y)]
        blocks_for_blue = [(0, x)]
    elif t == 2:
        blocks_for_green = [(0, y), (0, y+1)]
        blocks_for_blue = [(0, x), (1,x)]
    else:
        blocks_for_green = [(0, y), (1, y)]
        blocks_for_blue = [(0, x), (0,x+1)]

    # move
    move(green, blocks_for_green)
    move(blue, blocks_for_blue)

    # print("=====green======")
    # for g in green:
    #     print(*g)
    # print("=====blue======")
    # for g in blue:
    #     print(*g)
    
    # check
    ans += check_and_delete(green)
    ans += check_and_delete(blue)

    # check special row
    check_special_row(green)
    check_special_row(blue)

print(ans)

cnt = 0
for g in green:
    cnt += sum(g)
for b in blue:
    cnt += sum(b)
print(cnt)

        









