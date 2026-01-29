"""
12:45

(원반의 번호, 원판에서의 위치)
(i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)
(i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)

0. x, d, k
1. x의 배수인 원판을 d 방향으로 k칸 회전, d가 0이면 시계방향, d가 1이면 반시계
2. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것 탐색
    1. 그러한 수가 있으면 원판에 인접하면서 같은 수 삭제
    2. 없으면 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고 작은 수는 1 더함
원판을 T번 회전 시켰을 때 원판에 적힌 수의 합?

O(T*N**2): 12.5만
1. rotation
2. bfs
3. update
    
"""
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(circles): 
    plag = False
    
    for row in range(n):
        for col in range(m):
            if circles[row][col] == 0: continue
        
            q = deque([(row, col)])
            num = circles[row][col]
            # circles[row][col] = 0

            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    
                    # 같은 원판 안에서 보정
                    if ny == -1: ny = m-1
                    elif ny == m: ny = 0

                    if 0<=nx<n:
                        if circles[nx][ny] == num:
                            q.append((nx,ny))
                            circles[nx][ny] = 0

                            circles[row][col] = 0
                            plag = True

    return plag


from collections import deque
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

circles = [deque(list(map(int, input().split()))) for _ in range(n)]
rotation_orders = [list(map(int, input().split())) for _ in range(t)]


for x, d, k in rotation_orders:
    
    # rotation
    for nx in range(x-1, n, x):
        if d == 0: # 시계 방향
            circles[nx].rotate(k) # 맨 뒤를 앞으로, 시계방향
        else: # 반시계
            circles[nx].rotate(-k)
    
    # print("==="*10)
    # for c in circles:
    #     print(*c)

    # check
    plag = bfs(circles)
    

        # for a, b in del_list:
        #     circles[a][b] = 0
    
    if not plag:
        cnt = 0
        total = 0
        for i in range(n):
            for j in range(m):
                if circles[i][j] != 0:
                    total += circles[i][j]
                    cnt += 1
        if cnt == 0:
            continue

        mean = total/cnt

        for i in range(n):
            for j in range(m):
                if circles[i][j] == 0: continue
                if circles[i][j] > mean:
                    circles[i][j] -= 1
                elif circles[i][j] < mean:
                    circles[i][j] += 1
    # print("==="*10)
    # for c in circles:
    #     print(*c)

total = 0
for c in circles:
    total += sum(c)
print(total)


