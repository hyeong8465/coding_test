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

# 1차 필터, 진실을 알고 있는 사람이 있는 파티
# filter1 = []
cnt = 0
party_idx = set(range(0,m))
while True:
    # print(11111, party_idx)
    op = ppl_true.copy()
    # print(op)
    temp_idx = set()
    for idx in party_idx:
        pos = 0
        for p in parties[idx][1:]:
            if p in ppl_true:
                pos = 1
                break
        if pos == 1: # 진실을 아는 사람이 있는 파티
            for p in parties[idx][1:]:
                ppl_true.add(p)
            cnt+=1
            temp_idx.add(idx)
        # else: # 진실을 모르는 파티
    # if len(temp_idx) == 0:
    #     break
    # print(temp_idx)
    party_idx = party_idx - temp_idx
    # print(op)
    # print(ppl_true)
    # print(cnt)
    if len(op) == len(ppl_true):
        break
print(m-cnt) 