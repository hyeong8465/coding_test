a = input()
b = input()

lcs = [[0]*(len(a)+1) for _ in range(len(b)+1)]

for row in range(1,len(b)+1):
    for col in range(1,len(a)+1):
        if b[row-1] == a[col-1]:
            lcs[row][col] = lcs[row-1][col-1]+1
        else:
            lcs[row][col] = max(lcs[row-1][col], lcs[row][col-1])
print(lcs[-1][-1])

# for l in lcs:
#     print(l)

x = len(lcs)-1
y = len(lcs[0])-1
dx = [-1,0,-1]
dy = [0,-1,-1]

ans = ''
while True:
    # print(x,y)
    if lcs[x][y] == 0:
        break
    if b[x-1] == a[y-1]:
        ans += b[x-1]
        x-=1
        y-=1
        continue
    
    plag = False
    for i in range(3):
        nx = x+dx[i]
        ny = y+dy[i]
        if lcs[nx][ny] == lcs[x][y]:
            x = nx
            y = ny
            plag = True
            break
    if plag:
        continue
    x += dx[2]
    y += dy[2]


print(ans[::-1])
    



