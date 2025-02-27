"""
36진법의 수 n개 입력
36진법 숫자에서 k개 선택
n개의 수 모두에서 나타난 숫자를 z로 바꿈

"""
import sys
input = sys.stdin.readline

# 10 -> 36
def trans(n,k):
    if k == 0:
        return '0'
    ans = ''
    while k:
        if k%n>9:
            ans += chr(55+k%n)
        else:
            ans += str(k%n)
        k//=n
    return ans[::-1]

n = int(input())
arr = [input().rstrip() for _ in range(n)]
dic = {}
for a in arr:
    for i,j in enumerate(list(a)[::-1]):
        if j.isdigit():
            if j not in dic:
                dic[j] = (ord('Z')-55 - int(j))*(36**i)
            else:
                dic[j] += (ord('Z')-55 - int(j))*(36**i)
        else:
            if j not in dic:
                dic[j] = (ord('Z') - ord(j))*(36**i)
            else:
                dic[j] += (ord('Z') - ord(j))*(36**i)

# for i,j in dic.items():
#     dic[i] = (j, (ord('Z') - ord(i))*j)
k = int(input())

dic_sort = sorted(dic.items(), key = lambda x: -x[1])
# print(dic_sort)

val = sum([d[1] for d in dic_sort[:k]])
# print(val)
ans = 0
for a in arr:
    ans += int(a,36)
# print(ans)
ans+=val
# print(ans)

print(trans(36, ans))

# print(ans)
# print(int('31YUB',36))
# print(int('ZZZZZZZZZ',36))






