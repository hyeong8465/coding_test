n = int(input())

cnt = 0
for _ in range(n):
    text = input()
    ot = text[0]
    a = set(text[0])
    flag = True
    
    for i in range(1,len(text)):
        if text[i] in a:
            if ot != text[i]:
                flag = False
                break
        else:
            ot = text[i]
            a.add(text[i])
    
    if flag:
        cnt += 1
print(cnt)
