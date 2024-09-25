import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    n, m = map(int, input().split()) # 세로, 가로
    visited = [[False]*m for _ in range(n)]
    answer = [[-1]*m for _ in range(n)]
    
    # 경로 받기
    arr = []
    for i in range(n):
        temp = list(map(int, input().rstrip().split()))
        arr.append(temp)
        for idx, j in enumerate(temp):
            if j == 2:
                start = (i,idx,0)
                answer[start[0]][start[1]] = 0
            elif j == 0:
                answer[i][idx] = 0
    
    q = deque()
    q.append(start)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        r,c,cnt = q.popleft()
        for i in range(4):
            pr = r + dx[i]
            pc = c + dy[i]
            if pr <= -1 or pr >= n or pc <= -1 or pc >= m:
                continue
            else:
                if arr[pr][pc] == 1 and visited[pr][pc] == False:
                    q.append((pr,pc,cnt+1))
                    answer[pr][pc] = cnt+1
                    visited[pr][pc] = True
                elif arr[pr][pc] == 0:
                    answer[pr][pc] = 0
    
    for i in answer:
        for j in i:
            print(j, end = ' ')
        print('')
                
bfs()