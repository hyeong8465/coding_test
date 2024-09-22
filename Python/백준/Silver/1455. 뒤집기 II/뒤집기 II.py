def switch(row, col):
    for r_i in range(row+1):
        for c_i in range(col+1):
            coin[r_i][c_i] = -1*coin[r_i][c_i]
            # print(coin)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coin = []
for _ in range(n):
    temp = input().rstrip()
    coin.append([1 if int(temp[x]) == 1 else -1 for x in range(m)])
# print(coin)

count = 0
for r in range(n-1, -1, -1):
    for c in range(m-1, -1, -1):
        if coin[r][c] == 1:
            switch(r,c)
#            print(coin)
            count += 1
print(count)