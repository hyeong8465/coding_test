"""
13:36

한 승객을 태워 목적지로 이동시키는 일을 M번 반복

현재 위치에서 최단 거리가 가장 짧은 승객을 먼저 고름
    그런 승객이 여러 명이명, 행 번호가 작은, 열 번호가 작은 승객부터 고름
택시와 승객이 같은 위치에 있으면 최단거리는 0
1칸 이동에 연료 1소모
목적지에 성공적으로 이동시키면, 소모한 연료의 두배 획득
연료가 바닥나면 실패, 업무 종료
이동과 동시에 연료 바닥은 실패로 간주하지 않음
모든 승객을 성공적으로 데려다 줄 수 있는가? 그렇다면 남은 연료의 양은?

bfs
O(M*N**2*2) M*bfs*2 -> 16만

1. 가장 가까운 고객 탐색 bfs
2. 해당 고객의 목적지까지 bfs

"""
from collections import deque
import sys
input = sys.stdin.readline

n, m, fuel = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

x, y = map(int, input().split())
x = x-1
y = y-1

customers = {}
for _ in range(m):
    start_x, start_y, end_x, end_y = map(int, input().split())
    customers[(start_x-1, start_y-1)] = (end_x-1, end_y-1)

# 이걸로 우선순위 조건이 충분한가?
# 상, 좌, 우, 하
dx = [-1,0,0,1]
dy = [0,-1,1,0]

def find_customer(start_x, start_y): # return start_x, start_y, 거리 
    if (start_x, start_y) in customers:
        return [(start_x, start_y, 0)]
    
    visited = [[False] * n for _ in range(n)]
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True

    temp = []
    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    q.append((nx,ny,dist+1))
                    visited[nx][ny] = True
                    if (nx, ny) in customers:
                        temp.append((nx, ny, dist+1))
    temp.sort(key = lambda x:(x[2], x[0], x[1]))
    return temp

def find_destination(start_x, start_y, end_x, end_y):
    # print(111, start_x, start_y, end_x, end_y)
    if start_x == end_x and start_y == end_y:
        return (end_x, end_y, 0)
    
    visited = [[False] * n for _ in range(n)]
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True

    while q:
        # print(q)
        x, y, dist = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    if nx == end_x and ny == end_y:
                        return (nx, ny, dist+1)
                    q.append((nx,ny,dist+1))
                    visited[nx][ny] = True
    return -1 # 목적지에 도착할 수 없는 경우

# main
for _ in range(m):
    temp = find_customer(x, y)
    
    if len(temp) == 0:
        print(-1)
        quit()
    # print(temp)
    start_x, start_y, dist = temp[0]
    # print(start_x, start_y, dist)
    
    if fuel - dist < 0:
        print(-1)
        quit()
    fuel -= dist

    end_x, end_y = customers[(start_x, start_y)]
    del customers[(start_x, start_y)]
    
    temp = find_destination(start_x, start_y, end_x, end_y)
    
    if temp == -1:
        print(-1)
        quit()
    
    x, y, dist = temp 
    # print(x,y,dist)

    if fuel-dist < 0:
        print(-1)
        quit()
    
    fuel -= dist
    
    fuel += dist*2
    # print(fuel)
print(fuel)
    

"""
엣지 케이스에 조심
1. 같은 거리에서 우선 순위
2. 


"""
    
    





