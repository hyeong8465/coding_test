from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(blind = False):
    visited = [[False] * n for _ in range(n)]
    
    answer_norm = []
    answer_blind = []

    for r in range(n):
        for c in range(n):
            if visited[r][c] == True:
                continue
            q = deque([[r,c,grid[r][c]]]) # 시작
            visited[r][c] = True

            if not blind:
                answer_norm.append(c)
                while q:
                    x,y,c = q.popleft()
                    for i in range(4):
                        px, py = x+dx[i], y+dy[i]
                        if px <= -1 or px >= n or py <= -1 or py >= n:
                            continue
                        if visited[px][py] == False and grid[px][py] == c: # 안 갔고, 색이 같으면 감
                            q.append([px,py,c])
                            visited[px][py] = True
            else:
                answer_blind.append(c)
                while q:
                    x,y,c = q.popleft()
                    for i in range(4):
                        px, py = x+dx[i], y+dy[i]
                        if px <= -1 or px >= n or py <= -1 or py >= n:
                            continue
                        if c == 'R' or c == 'G':
                            if visited[px][py] == False and (grid[px][py] == 'R' or grid[px][py] == 'G'): # 안 갔고, 색이 같으면 감
                                q.append([px,py,c])
                                visited[px][py] = True
                        else:
                            if visited[px][py] == False and grid[px][py] == c: # 안 갔고, 색이 같으면 감
                                q.append([px,py,c])
                                visited[px][py] = True
    if blind:
        return len(answer_blind)
    else:
        return len(answer_norm)

print(str(bfs(blind = False))+' '+str(bfs(blind = True)))