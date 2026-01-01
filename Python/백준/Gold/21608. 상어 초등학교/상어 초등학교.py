"""
12:20

인접: 상하좌우 1칸씩

규칙
1. 좋아하는 학생이 입전한 킨에 가장 많은 칸
1-1. 비어있는 칸이 가장 많은 칸
1-2. 행 번호가 가장 작은 칸 -> 열 번호가 가장 작은 칸

시뮬, 구현

로직
1. 빈칸을 순회하면서 좋아하는 학생과 가장 많이 인접한 칸 탐색

만족도 계산

시간 복잡도 계산
N은 최대 20
전체 학생: N^2
각 학생마다 전체 자리 순회: N^2
1초 가능
"""
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
    num_to_like[a] = (b,c,d,e)

positions = [[0]*n for _ in range(n)]

for stu, likes in num_to_like.items():
    l_cnt = -1
    e_cnt = -1
    pos = None
    for i in range(n):
        for j in range(n):
            # print("stu", stu)
            # print(i,j)
            # print("pos", pos)
            # print("기준:", l_cnt, e_cnt)


            if positions[i][j] != 0:
                continue

            like_cnt, empty_cnt = check(stu, likes, i, j)
            
            # print(like_cnt, empty_cnt)
            
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
    # for p in positions:
    #     print(*p)
    # print("==="*10)

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

            

            
            





