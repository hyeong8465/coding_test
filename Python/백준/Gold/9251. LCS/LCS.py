a = input()
b = input()

lcs = [[0]*(len(a)+1) for _ in range(len(b)+1)]

# if a == b:
#     print(len(a))
#     quit()

for row in range(1,len(b)+1):
    for col in range(1,len(a)+1):
        if b[row-1] == a[col-1]:
            lcs[row][col] = lcs[row-1][col-1]+1
        else:
            lcs[row][col] = max(lcs[row-1][col], lcs[row][col-1])
print(lcs[-1][-1])
# for i in lcs:
#     print(i)