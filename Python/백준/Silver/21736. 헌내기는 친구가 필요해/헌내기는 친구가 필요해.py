import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

arr = []
for _ in range(n):
    temp = list(input().rstrip())
    arr.append(temp)
# print(arr)

for r in range(n):
    for c in range(m):
        if arr[r][c] == 'I':
            s = (r,c)
            # print(s)
            break
        
def bfs():
    visited = [[False]*m for _ in range(n)]
    q = deque([s])
    visited[s[0]][s[1]] = True
    answer = 0
    while q:
        r,c = q.popleft()
        for i in range(4):
            pr, pc = r+dx[i], c+dy[i]
            if 0 <= pr < n and 0<= pc < m and not visited[pr][pc] :
                if arr[pr][pc] == 'P':
                    answer += 1
                    q.append((pr,pc))
                    visited[pr][pc] = True
                elif arr[pr][pc] == 'X': 
                    visited[pr][pc] = True
                else:
                    q.append((pr,pc))
                    visited[pr][pc] = True
    # print(answer)
    if answer == 0:
        return 'TT'
    else:
        return answer

print(bfs())