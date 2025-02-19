h, w, n, m = map(int, input().split()) # 행, 열, 세로 간격, 가로 간격

result = 0
if h%(n+1) == 0:
    r = h/(n+1)
else:
    r = h//(n+1) + 1

if w%(m+1) == 0:
    c = w/(m+1)
else:
    c = w//(m+1) + 1
# print(r,c)
print(int(r*c))

# c = w/(m+1)

# # for r in range(0, h, n+1):
# #     for c in range(0, w, m+1):
# #         print(r,c)
# #         result += 1
# print(result)