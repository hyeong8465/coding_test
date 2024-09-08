dic = {}
for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
    dic[str(i)] = 0
word = input()
for i in word:
    dic[str(i)] += 1
for i in dic.values():
    print(i, end=' ')