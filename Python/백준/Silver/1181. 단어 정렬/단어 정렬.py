N = int(input())

# dic 문자:길이

dic = {}
for _ in range(N):
    val = input()
    dic[val] = len(val)

dic1 = {}

for i in set(dic.values()):
    dic1[i] = []

for val, key in dic.items():
    dic1[key].append(val)

for i in sorted(dic1.keys()):
    dic1[i].sort()
    for j in dic1[i]:
        print(j)