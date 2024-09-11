import sys
input = sys.stdin.readline

M, N = map(int,input().rstrip().split())
arr = []
for _ in range(M):
    temp = input().rstrip()
    arr.append(temp)
color_W = ['W','B'] * 4 + ['B','W'] * 4 + ['W','B'] * 4 + ['B','W'] * 4 + ['W','B'] * 4 + ['B','W'] * 4 + ['W','B'] * 4 + ['B','W'] * 4
color_B = ['B','W'] * 4 + ['W','B'] * 4 + ['B','W'] * 4 + ['W','B'] * 4 + ['B','W'] * 4 + ['W','B'] * 4 + ['B','W'] * 4 + ['W','B'] * 4
answer = []
# 8x8 자르기
for col in range(0,N-8+1):    
    for row in range(0, M-8+1):
        temp = []
        for r in range(row,row+8):
            temp.append(arr[r][col:col+8])
        count = 0
        idx = 0
        for r in range(8):
            for c in range(8):
                if temp[r][c] == color_W[idx]: # 색이 같으면
                    pass
                else:
                    count += 1
                idx += 1
        answer.append(count)
        count = 0
        color = ['W','B'] * 32
        idx = 0
        for r in range(8):
            for c in range(8):
                # print('W', temp[r][c], color)
                if temp[r][c] == color_B[idx]: # 색이 같으면
                    pass
                else:
                    count += 1
                idx += 1
        answer.append(count)
print(min(answer))