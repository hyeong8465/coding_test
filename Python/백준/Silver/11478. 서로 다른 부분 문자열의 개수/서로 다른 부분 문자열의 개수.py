text = input()
result = set()
for i in range(len(text)):
    for j in range(i,len(text)):
        # print(text[i:j+1])
        if text[i:j+1] not in result:
            result.add(text[i:j+1])
# print(result)
print(len(result))
