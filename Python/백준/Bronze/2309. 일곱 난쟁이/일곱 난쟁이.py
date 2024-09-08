arr = []
for _ in range(9):
    a = int(input())
    arr.append(a)
arr.sort()
idx = []
for i in range(9):
    for j in range(i+1,9):
        idx.append([i,j])
# print(idx)
org_idx = set(range(9))
for i in idx:
    temp_idx = org_idx - set(i)
    # print(temp_idx)
    ans = 0
    for j in temp_idx:
        ans += arr[j]
    if ans == 100:
        for k in temp_idx:
            print(arr[k])
        quit()