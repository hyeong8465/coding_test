"""
09:40
문자열

주어진 문자열의 순서를 바꿔서 팰린드롬 만들기
최대 50자
2초
"""
string = input()
dic = {}
for s in string:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
# 홀수가 하나 이하인지 확인
odd = []
for k, v in dic.items():
    if v % 2 == 1:
        odd.append(k)

if len(odd) > 1: # 둘 이상
    print("I'm Sorry Hansoo")
    quit()

# 하나 이하
if len(string) % 2 == 0: # 짝수
    left = []
    for k, v in dic.items():
        left += [k]*(v//2)
    left.sort()
    l = ''.join(left)
    r = l[::-1]
    ans = l+r

else: # 홀수
    left = []
    for k, v in dic.items():
        left += [k]*(v//2)
    left.sort()
    l = ''.join(left)
    r = l[::-1]
    center = odd[0]
    ans = l+center+r
    
    
print(ans)