n = int(input())

arr = []
max_len = 0
for _ in range(n):
    temp = input()
    max_len = max(max_len, len(temp))
    arr.append(temp)

dic = {}
for a in arr:
    length = len(a)
    for i in range(length):
        if a[i] in dic:
            dic[a[i]] += int(10**(length-i-1))
        else:
            dic[a[i]] = int(10**(length-i-1))
dic_list = [(k,v) for k,v in dic.items()]
dic_list.sort(key = lambda x: -x[1])

num = 9
result = 0
for a, b in dic_list:
    result += num*b
    num -= 1
print(result)