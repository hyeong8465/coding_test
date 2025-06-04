"""
21:37

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여있는 수들의 합을 최대로

시간제한: 2초
n,m: 최대 500
250000 * 4 * 20 = 20만

테트로미노는 그냥 4칸 dfs -> ㅜ 모양 고려 불가 그냥 노가다 ㄱㄱ
sol 10:25

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

tetromino = [[(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,0), (2,0), (3,0)], # ㅡ, ㅣ
             [(0,0), (1,0), (0,1), (1,1)], # ㅁ
             [(0,0), (1,0), (2,0), (2,1)], [(0,0),(1,0),(0,1),(0,2)], [(0,0),(0,1),(1,1),(2,1)], [(0,0), (0,1),(0,2),(-1,2)], # ㄴ
             [(0,0), (1,0), (2,0), (2,-1)], [(0,0),(0,1),(0,2),(1,2)], [(0,0),(0,1),(1,0),(2,0)], [(0,0), (1,0),(1,1),(1,2)], # 좌우 대칭
             [(0,0), (1,0), (1,1), (2,1)], [(0,0), (0,1), (-1,1), (-1,2)],
             [(0,0), (1,0), (1,-1), (2,-1)], [(0,0), (0,1), (1,1), (1,2)],
             [(0,0), (0,1), (1,1), (0,2)], [(0,0), (-1,1), (0,1), (1,1)], [(0,0), (0,1),(-1,1),(0,2)], [(0,0), (1,0), (2,0), (1,1)] # ㅜ, ㅓ, ㅗ, ㅏ
]

ans = 0
for x in range(n):
    for y in range(m):
        for tet in tetromino:
            temp = 0
            for dx,dy in tet:
                nx = x+dx
                ny = y+dy
                if 0<=nx<n and 0<=ny<m:
                    temp += arr[nx][ny]
                else:
                    break
            ans = max(ans, temp)
print(ans)







# visited = [[False] * m for _ in range(n)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]


# def dfs(x, y, val, cnt):
#     global ans
#     if cnt == 4:
#         print('끝은', x, y, val)
#         ans = max(ans, val)
#         return None
    
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<n and 0<=ny<m:
#             if not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 dfs(nx, ny, val+arr[nx][ny], cnt+1)
#                 visited[nx][ny] = False

# ans = 0
# for a in range(n):
#     for b in range(m):
#         print('지금 위치:', a,b)
#         dfs(a,b,arr[a][b],1)
# print(ans)
        













