"""
20:11
백트래킹
1. 가로로 필터링
2. 세로로 필터링
3. 네모로 필터링


"""
arr = [list(map(int, input().split())) for _ in range(9)]

def check(x,y,num):
    if num in arr[x]:
        return False
    
    for i in range(9):
        if arr[i][y] == num:
            return False
    
    for i in range(x//3*3,x//3*3+3):
        for j in range(y//3*3,y//3*3+3):
            if arr[i][j] == num:
                return False
    return True

pos = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            pos.append((i,j))

def solve_sudoku():
    for i,j in pos:
        if arr[i][j] == 0:
            for n in range(1,10):
                if check(i,j,n):
                    arr[i][j] = n
                    if solve_sudoku():
                        return True
                arr[i][j] = 0
            return False
    return True

solve_sudoku()
for a in arr:
    print(*a)

                



