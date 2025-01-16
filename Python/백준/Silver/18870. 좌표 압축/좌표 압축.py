n = int(input())
arr = list(map(int, input().split()))

arr_set = list(set(arr))
arr_set.sort()
# print(arr_set)

dic = {}
for i in range(len(arr_set)):
    dic[arr_set[i]] = i
answer = [dic[i] for i in arr]

print(*answer)
    


