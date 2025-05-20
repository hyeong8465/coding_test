n, m = map(int, input().split())
arr = list(map(int, input().split()))

pos = sorted([x for x in arr if x > 0], reverse=True)
neg = sorted([-x for x in arr if x < 0], reverse=True)

ans = 0
distances = []

# 양수 묶음
for i in range(0, len(pos), m):
    distances.append(pos[i])
# 음수 묶음
for i in range(0, len(neg), m):
    distances.append(neg[i])

# 가장 먼 거리 1개만 편도
ans += max(distances)

# 나머지는 왕복
for d in distances:
    if d != max(distances):
        ans += 2 * d

print(ans)