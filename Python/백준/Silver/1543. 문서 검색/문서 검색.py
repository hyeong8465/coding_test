"""
try1: stack에 하나씩 쌓고 문자 길이만큼 확인
try2: 단순 슬라이싱

"""
doc = input()
text = input()

idx = 0
ans = 0
d = len(doc)
t = len(text)

while idx+t <= d:
    if doc[idx:idx+t] == text:
        ans += 1
        idx += t
    else:
        idx += 1
print(ans)