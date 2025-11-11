n = int(input())

coor = [tuple(map(int, input().split())) for _ in range(n)]

x1, y1 = coor[0]
val = 0
for i in range(2,n):
    v1_x, v1_y = coor[i-1][0]-x1, coor[i-1][1]-y1
    v2_x, v2_y = coor[i][0]-x1, coor[i][1]-y1
    val += v1_x*v2_y-v1_y*v2_x

print(round(abs(val)/2, 3))