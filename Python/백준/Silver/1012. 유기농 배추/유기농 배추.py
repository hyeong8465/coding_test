import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    T = int(input())
    for _ in range(T):
        col_num, row_num, K = map(int, input().split()) # m - 가로길이, n - 세로길이
        visited = [[False]*col_num for _ in range(row_num)]
        baechu = [[0]*col_num for _ in range(row_num)]

        cnt = 0
    
        for _ in range(K):
            col, row = map(int, input().split())
            baechu[row][col] = 1
        
        q = deque()
        for i in range(row_num):
            for j in range(col_num):
                if baechu[i][j] == 1 and visited[i][j] == False: # 시작점 탐색
                    cnt += 1
                    q.append((i,j))
                    visited[i][j] = True # 방문 처리
                    dx = [1,0,-1,0]
                    dy = [0,1,0,-1]
                    while q:
                        # print(q)
                        x,y = q.popleft()
                        for k in range(4):
                            px = x + dx[k]
                            py = y + dy[k]
                            if 0 <= px < row_num and 0 <= py < col_num:
                                if baechu[px][py] == 1 and visited[px][py] == False:
                                    q.append((px, py))
                                    visited[px][py] = True
        print(cnt)

bfs()