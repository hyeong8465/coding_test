N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))


weight = [x[0] for x in people]
height = [x[1] for x in people]

for i, p in enumerate(people):
    w, h = p[0], p[1]
    answer = 0
    temp_idx = []
    for j, w_i in enumerate(weight):
        if w_i > w:
            temp_idx.append(j)
    for idx in temp_idx:
        if height[idx] > h:
            answer += 1
    print(answer+1)