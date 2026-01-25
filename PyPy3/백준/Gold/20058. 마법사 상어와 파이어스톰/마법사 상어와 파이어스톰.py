import sys
from collections import deque
input = sys.stdin.readline

def rotate(sub_matrix):
    size = len(sub_matrix)
    rotated_sub_matrix = [[0]*size for _ in range(size)]

    for i in range(size):
        col = size-1-i
        for row, val in enumerate(sub_matrix[i]):
            rotated_sub_matrix[row][col] = val
    
    return rotated_sub_matrix

def is_reduce(x, y):
    ice_cnt = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<2**n and 0<=ny<2**n:
            if ices[nx][ny] != 0:
                ice_cnt += 1
    
    if ice_cnt < 3:
        return True
    
    return False

def bfs(x,y):
    cnt = 1
    q = deque([(x,y)])
    visited[x][y] = True

    while q:
        
        nx, ny = q.popleft()
        for i in range(4):
            nnx, nny = nx+dx[i], ny+dy[i]
            
            if 0<=nnx<2**n and 0<=nny<2**n:
                if ices[nnx][nny] != 0 and not visited[nnx][nny]:
                    q.append((nnx,nny))
                    visited[nnx][nny] = True
                    cnt += 1

    return cnt



n, q = map(int, input().split())
N_SIZE = 2**n
ices = [list(map(int, input().split())) for _ in range(2**n)]
l_list = list(map(int, input().split()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[False]*2**n for _ in range(2**n)]

for q_i in range(q):
    l = l_list[q_i]
    
    # move
    for i in range(0, N_SIZE, 2**l):
        for j in range(0, N_SIZE, 2**l):
            
            submatrix = []
            for ii in range(i,i+2**l):
                submatrix.append(ices[ii][j:j+2**l])
            # print(submatrix)

            rotated_sub_matrix = rotate(submatrix)

            for idx, ii in enumerate(range(i,i+2**l)):
                ices[ii][j:j+2**l] = rotated_sub_matrix[idx]
    
    # check
    reduce_candidates = []
    for i in range(N_SIZE):
        for j in range(N_SIZE):
            if is_reduce(i,j):
                reduce_candidates.append((i,j))
    
    # reduce
    for i, j in reduce_candidates:
        if ices[i][j] != 0: # 수정
            ices[i][j] -= 1

    # print("==="*10)
    # for ice in ices:
    #     print(*ice)

ans = 0
for ice in ices:
    ans += sum(ice)
print(ans)

# for ice in ices:
#     print(*ice)

ans = 0
for i in range(N_SIZE):
    for j in range(N_SIZE):
        if not visited[i][j] and ices[i][j] != 0: # 수정
            # print((i,j))
            ans = max(ans, bfs(i,j))
            # for v in visited:
            #     print(*v)

print(ans)