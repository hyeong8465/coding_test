"""
21:24
백트래킹, dfs

5명이 연결되어 있는 경우가 있는지?
0 - 1 - 2 - 3 - 0
    ㄴ 4

0 - 1 - 4
|   |
3 - 2
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
visited = [False]*n

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

res = 0
def dfs(start, cnt):
    global res
    if res == 1:
        return
    if cnt == 5:
        res = 1
        return
    
    for a in arr[start]:
        if not visited[a]:
            visited[a] = True
            dfs(a, cnt+1)
            visited[a] = False

for i in range(n):
    visited[i] = True
    dfs(i,1)
    visited[i] = False
    if res == 1:
        break

print(res)