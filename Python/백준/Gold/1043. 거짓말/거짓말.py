n, m = map(int, input().split())
knowList = set(input().split()[1:])

parties = []
for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knowList: # 교집합이 있다면
            knowList = knowList.union(party) # 합집합으로 만듦

cnt = 0
for party in parties:
    if party & knowList:
        continue
    cnt += 1
print(cnt)