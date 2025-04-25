# sol 1
n, m = map(int, input().split())
ppl = list(map(int, input().split()))
if ppl[0] == 0:
    print(m)
    exit()

# 진실을 알고 있는 사람
ppl_true = set()
for p in ppl[1:]:
    ppl_true.add(p)

parties = [list(map(int, input().split())) for _ in range(m)]

cnt = 0
party_idx = set(range(0,m))
while True:
    olen = len(party_idx)
    temp_idx = set()
    for idx in party_idx: # 파티 인덱스에 대해서
        pos = False
        for p in parties[idx][1:]:
            if p in ppl_true:
                pos = True
                break
        if pos: # 진실을 아는 사람이 있는 파티
            for p in parties[idx][1:]:
                ppl_true.add(p)
            cnt += 1
            temp_idx.add(idx)
    party_idx = party_idx - temp_idx
    nlen = len(party_idx)
    if olen == nlen:
        break
print(m-cnt) 