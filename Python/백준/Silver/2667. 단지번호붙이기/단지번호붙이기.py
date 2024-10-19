import sys
from collections import deque

n = int(input())
apartments = [list(map(int,list(input().rstrip()))) for _ in range(n)]
# print(apartments)
def bfs():
    ans = []
    visited = [[False]* n for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for r in range(n):
        for c in range(n):
            if apartments[r][c] == 0 or visited[r][c]:
                continue
            num = 1
            # print((r,c))
            # for i in visited:
                # print(i)
            q = deque([(r, c)])
            
            visited[r][c] = True
            while q:
                x, y = q.popleft()
                for i in range(4):
                    px, py = x+dx[i], y+dy[i]
                    if (0 <= px < n and 0 <= py < n) and not visited[px][py] and apartments[px][py] == 1:
                        q.append((px, py))
                        visited[px][py] = True
                        num += 1
            ans.append(num)
    return ans
val = bfs()
val.sort()
print(len(val))
for i in val:
    print(i)