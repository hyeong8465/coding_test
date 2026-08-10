from itertools import product
import sys

input = sys.stdin.readline

n = int(input())
original_boards = [list(map(int, input().split())) for _ in range(n)]
directions = ["l", "r", "u", "d"]
choosen_directions = product(directions, repeat=5)

ans = 0
for row in original_boards:
    ans = max(ans, max(row))

for choosen_direction in choosen_directions:
    boards = [original_board[:] for original_board in original_boards]
    
    for direction in choosen_direction:
        check = [[False] * n for _ in range(n)]
        
        if direction == "r":
            for row in range(n):
                for col in range(n-2, -1, -1):
                    if boards[row][col] == 0: continue
                    
                    start = col
                    while start < n-1:
                        if boards[row][start] == boards[row][start+1] and not check[row][start+1]:
                            boards[row][start+1] *= 2
                            boards[row][start] = 0
                            check[row][start+1] = True
                            break
                        elif boards[row][start+1] == 0:
                            boards[row][start+1] = boards[row][start]
                            boards[row][start] = 0
                            start += 1
                        else:
                            break
                            
        elif direction == "l":
            for row in range(n):
                for col in range(1, n):
                    if boards[row][col] == 0: continue
                    
                    start = col
                    while start > 0:
                        if boards[row][start] == boards[row][start-1] and not check[row][start-1]:
                            boards[row][start-1] *= 2
                            boards[row][start] = 0
                            check[row][start-1] = True
                            break
                        elif boards[row][start-1] == 0:
                            boards[row][start-1] = boards[row][start]
                            boards[row][start] = 0
                            start -= 1
                        else:
                            break
                            
        elif direction == "u":
            for row in range(1, n):
                for col in range(n):
                    if boards[row][col] == 0: continue
                    
                    start = row
                    while start > 0:
                        if boards[start][col] == boards[start-1][col] and not check[start-1][col]:
                            boards[start-1][col] *= 2
                            boards[start][col] = 0
                            check[start-1][col] = True
                            break
                        elif boards[start-1][col] == 0:
                            boards[start-1][col] = boards[start][col]
                            boards[start][col] = 0
                            start -= 1
                        else:
                            break
                            
        elif direction == "d":
            for row in range(n-2, -1, -1):
                for col in range(n):
                    if boards[row][col] == 0: continue
                    
                    start = row
                    while start < n-1:
                        if boards[start][col] == boards[start+1][col] and not check[start+1][col]:
                            boards[start+1][col] *= 2
                            boards[start][col] = 0
                            check[start+1][col] = True
                            break
                        elif boards[start+1][col] == 0:
                            boards[start+1][col] = boards[start][col]
                            boards[start][col] = 0
                            start += 1
                        else:
                            break
                            
    for board in boards:
        ans = max(ans, max(board))

print(ans)