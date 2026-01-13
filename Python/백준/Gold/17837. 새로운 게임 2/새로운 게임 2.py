"""
13:18

말의 개수: k개
하나의 말 위에 다른 말 올릴 수 있음

칸의 색: 흰, 빨, 파 
번호, 이동방향

말이 4개 이상 쌓이면 게임 종료

이동하려는 칸이
흰: 
1. 그 칸으로 이동
2. 이미 그 칸에 말이 있다면 가장 위에 쌓음
3. 이동하려는 말의 위에 있는 모든 말이 같이 이동
빨:
1. 이동한 후 A번 말과 그 위에 모든 말의 순서를 반대로
-> 뒤집어서 쌓기
파, 체스판을 벗어나는 경우:
1. 이동 방향을 반대로 하고 한 칸 이동
2. 이동하려는 칸이 다시 파란색이면 이동하지 않고 가만히 있음



시뮬레이션


"""
n, k = map(int, input().split())

chess = [list(map(int, input().split())) for _ in range(n)]
horses_list = [[[] for _ in range(n)] for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

horses_dict = {}
for i in range(k):
    x,y,d = map(int, input().split())
    horses_dict[i+1] = [x-1,y-1,d-1]
    horses_list[x-1][y-1].append(i+1)

for turn in range(1,1001):
    # print("==========")
    for horse in range(1,k+1):
        x,y,d = horses_dict[horse]

        nx, ny = x+dx[d], y+dy[d]

        if not(0<=nx<n and 0<=ny<n) or chess[nx][ny] == 2:
            # print("말번호", horse)
            
            # 방향 전환
            # print(d)
            if d == 0: d = 1
            elif d == 1: d = 0
            elif d == 2: d = 3
            elif d == 3: d = 2

            horses_dict[horse][2] = d
            # print(d)
            # 다시 이동
            nx, ny = x+dx[d], y+dy[d]
            # print(nx,ny)
            
            if not (0<=nx<n and 0<=ny<n) or chess[nx][ny] == 2: # 다시 파란칸이면
                continue

        if chess[nx][ny] == 0:
            idx = horses_list[x][y].index(horse)
            horses_list[nx][ny].extend(horses_list[x][y][idx:])
            if len(horses_list[nx][ny]) >= 4:
                print(turn)
                quit()

            for i in horses_list[x][y][idx:]:
                a,b,c = horses_dict[i]
                horses_dict[i] = [nx,ny,c]
            del horses_list[x][y][idx:]

        elif chess[nx][ny] == 1:
            idx = horses_list[x][y].index(horse)
            # print(idx)
            # horses_list[x][y][idx:].reverse()
            horses_list[nx][ny].extend(horses_list[x][y][idx:][::-1])
            if len(horses_list[nx][ny]) >= 4:
                print(turn)
                quit()

            for i in horses_list[x][y][idx:]:
                a,b,c = horses_dict[i]
                horses_dict[i] = [nx,ny,c]
            del horses_list[x][y][idx:]
        

        # for h in horses_list:
        #      print(*h)
        # print()
            

print(-1)