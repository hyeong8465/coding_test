
import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def check(stu, likes, x, y):
    like_cnt = 0
    empty_cnt = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if positions[nx][ny] in likes:
                like_cnt += 1
            elif positions[nx][ny] == 0:
                empty_cnt += 1
    # print(like_cnt, empty_cnt)
    return (like_cnt, empty_cnt)

n = int(input())
num_to_like = {}

for _ in range(n**2):
    a, b, c, d, e = map(int, input().split())
    num_to_like[a] = set([b,c,d,e])

positions = [[0]*n for _ in range(n)]

for stu, likes in num_to_like.items():
    l_cnt = -1
    e_cnt = -1
    pos = None
    for i in range(n):
        for j in range(n):

            if positions[i][j] != 0:
                continue

            like_cnt, empty_cnt = check(stu, likes, i, j)
            
            # 조건 1
            if like_cnt > l_cnt:
                l_cnt = like_cnt
                e_cnt = empty_cnt
                pos = (i,j)
                continue
            
            # 조건 2
            if like_cnt == l_cnt and empty_cnt > e_cnt:
                e_cnt = empty_cnt
                pos = (i,j)
                continue
    positions[pos[0]][pos[1]] = stu

# 점수 계산
ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        likes = num_to_like[positions[i][j]]
        for k in range(4):
            ni = i+dx[k]
            nj = j+dy[k]
            if 0<=ni<n and 0<=nj<n:
                if positions[ni][nj] in likes:
                    cnt += 1
        if cnt == 0:
            continue
        ans += 10**(cnt-1)
print(ans)
