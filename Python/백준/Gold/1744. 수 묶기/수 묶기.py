# 최적화
n = int(input())

pos = []
neg = []
zero = False
ans = 0

for _ in range(n):
    t = int(input())
    if t > 1:
        pos.append(t)
    elif t == 1: # t가 1이면 바로 더하는 게 값이 더 큼
        ans += 1
    elif t < 0:
        neg.append(t)
    else:
        zero = True

pos.sort(reverse = True)
neg.sort()

for i in range(0, len(pos), 2):
    if i + 1 >= len(pos):
        ans += pos[i]
    else:
        ans += pos[i]*pos[i+1]

for i in range(0,len(neg), 2):
    if i+1 >= len(neg):
        if not zero:
            ans += neg[i]
    else:
        ans += neg[i]*neg[i+1]

print(ans)