"""
구현, 시뮬?


18:01

"""
from collections import deque
n = int(input())

fishes = {}
eated = {}
for i in range(1,7):
    fishes[i] = []
    eated[i] = 0

arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j, t in enumerate(temp):
        if t != 0:
            if t != 9:
                fishes[t].append((i,j))
            else:
                shark = [i,j]
    arr.append(temp)
# arr[shark[0]][shark[1]]

# print(arr)
# print(shark)
# print(fishes)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(start):
    dis = [[-1]*n for _ in range(n)]
    dis[start[0]][start[1]] = 0
    edible = []
    
    visited = [[False]* n for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    q = deque([(start[0],start[1],0)])
    while q:
        x, y, c = q.popleft()
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]
            if 0<=px<n and 0<=py<n:
                if not visited[px][py] and arr[px][py] <= size:
                    dis[px][py] = c+1
                    visited[px][py] = True
                    q.append((px,py,c+1))
                    if 0<arr[px][py]<size:
                        edible.append((px,py))
    return dis, edible

size = 2
time = 0
eat_count = 0
while True:
    # print('start')
    # for a in arr:
    #     print(a)
    # # 먹을 수 있는 물고기 수집
    # edible = []
    # for k,v in fishes.items():
    #     if k < size:
    #         edible.extend(v)
    
    # 거리, 먹을 수 있는지 확인
    dis, edible = bfs(shark)
    edible.sort()
    # print(1111, edible)
    # for d in dis:
        # print(d)

    # 먹으러 갈 대상 선정
    val = float('inf')
    target = []
    for e in edible:
        if dis[e[0]][e[1]] == -1: # 먹으러 못 가는 경우
            continue
        else:
            if dis[e[0]][e[1]] < val:
                val = dis[e[0]][e[1]]
                target = e
    # print(333, val, target)
    
    # 먹으러 갈 대상이 없으면
    if len(target) == 0:
        break
    
    a, b = target

    time += val # 시간 추가
    eat_count += 1
    if eat_count == size: # 사이즈 변경
        eat_count = 0
        size += 1
    # print('size', size)
    arr[shark[0]][shark[1]] = 0
    shark = target # 위치 변경
    arr[a][b] = 9 # 빈칸
    # print(time)
    # print('=====')

print(time)
