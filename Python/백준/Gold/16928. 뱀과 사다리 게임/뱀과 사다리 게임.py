import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [[]]
for i in range(1,101):
    arr.append([i+1, i+2, i+3, i+4, i+5, i+6])

up = {}
for _ in range(n): # 상승
    u, v = map(int, input().split())
    up[u] = v
    arr[u].append(v)
down = {}
for _ in range(m): # 하강
    u, v = map(int, input().split())
    down[u] = v
    arr[u].append(v)

def bfs():
    visited = [False] * 101
    q = deque([[1, 0]]) # 1에서 시작
    visited[1] = True
    while q:
        pos, cnt = q.popleft()
        # print(pos, cnt)
        if pos == 100:
            return cnt
        else:
            for a in arr[pos]:
                if a >= 101:
                    continue
                if visited[a] == False:
                    if a in up:
                        q.append([up[a], cnt+1])
                        visited[a] = True
                        visited[up[a]] = True
                    elif a in down:
                        q.append([down[a], cnt+1])
                        visited[a] = True
                        visited[down[a]] = True
                    else:
                        q.append([a,cnt+1])
                        visited[a] = True
                    
                else:
                    continue
print(bfs())