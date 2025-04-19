"""
20:44


"""
n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dirs = list(map(int, input().split()))

# print(arr)

d = 6
u = 1
dice = [3, 4, 2, 5] # 맞은 편, 동, 서, 북, 남
dice_dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0
for dir in dirs:
    cnt+=1
    for i in range(4):
        if dir == i+1: # 방향을 찾으면
            # 이동
            x = x+dx[i]
            y = y+dy[i]
            if 0<=x<n and 0<=y<m: # 이동이 유효하면
                # 프린트
                od = d
                d = dice[i]
                u = 7-d
                print(dice_dic[u])
                
                # 주사위 수정
                if i == 0: # 동
                    dice[1] = od
                    dice[0] = 7-od
                elif i == 1: # 서
                    dice[0] = od
                    dice[1] = 7-od
                elif i == 2: # 북
                    dice[3] = od
                    dice[2] = 7-od
                else:
                    dice[2] = od
                    dice[3] = 7-od

                # 칸 수정
                if arr[x][y] == 0: # 해당 칸이 0이면
                    arr[x][y] = dice_dic[d]
                else:
                    dice_dic[d] = arr[x][y]
                    arr[x][y] = 0
            else:
                x = x-dx[i]
                y = y-dy[i]


    # print(f'{cnt} 번째 결과')
    # print(dice_dic)
    # print(dice)
    # for a in arr:
    #     print(a)
                

                    



        

