"""
(1,1) -> (n,m)

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,list(input().rstrip()))))

def bfs():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]    
    visited = [[False]*m for _ in range(n)]

    q = deque()
    q.append([0,0,1]) # (0,0)에서 시작
    visited[0][0] = True
    
    while q:
        x, y, cnt = q.popleft()
        if x == n-1 and y == m-1:
            return cnt
        
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]
            if px <= -1 or px >= n or py <= -1 or py >= m:
                continue
            else:
                if visited[px][py] == False and arr[px][py] == 1:
                    q.append([px,py, cnt+1])
                    visited[px][py] = True
                
    return cnt

print(bfs())