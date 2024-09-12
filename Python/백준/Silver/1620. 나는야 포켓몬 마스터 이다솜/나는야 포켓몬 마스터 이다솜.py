import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poke1 = {}
poke2 = {}
for i in range(N):
    temp = input().rstrip()
    poke1[i+1] = temp # 숫자로 검색
    poke2[temp] = i+1 # 이름으로 검색

for j in range(M):
    val = input().rstrip()
    try:
        print(poke1[int(val)])
    except:
        print(poke2[val])