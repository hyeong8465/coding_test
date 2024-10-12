import sys
from collections import deque

input = sys.stdin.readline 

n = int(input())
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
visited = [[False]*n for _ in range(n)]

q = deque([[0, 0, arr[0][0]]]) # 시작점 & 시작점의 스텝
visited[0][0] = True
dx = [1,0]
dy = [0,1]

def bfs():
    while q:
        # print(q)
        x, y, step = q.popleft()
        if x == n-1 and y == n-1:
            return "HaruHaru"
        for i in range(2):
            px, py = x+step*dx[i], y+step*dy[i]
            if px >= n or py >= n:
                continue
            else:
                if not visited[px][py]:
                    q.append([px, py, arr[px][py]])
                    visited[px][py] = True
    return "Hing"

print(bfs())