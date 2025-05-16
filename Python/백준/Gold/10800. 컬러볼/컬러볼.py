import sys
input = sys.stdin.readline

n = int(input())

# 입력
arr = []
for i in range(n):
    a, b = map(int, input().rstrip().split())
    arr.append((i,a,b))
arr.sort(key = lambda x: (x[2], x[1])) # 무게, 색상 기준 오름차순 정렬

ans = [0]*n # 정답 저장

temp = [0] * (n+2) # n+1번째는 총합

max_w = 0
cnt = 0
oc = 0
c_cnt = 0
for idx, c, w in arr:
    temp[c] += w
    temp[n+1] += w

    # 무게의 최대값 기록
    if w == max_w:
        cnt+=1
        if c == oc:
            c_cnt += 1
        else:
            c_cnt = 0
            oc = c
    else:
        max_w = w
        cnt = 0
        c_cnt = 0
        oc = c
    
    val = temp[n+1] - temp[c]
    # print(c_cnt)

    if w == max_w: # 무게의 최대값과 같으면
        val -= (cnt-c_cnt)*max_w

    ans[idx] = val

for a in ans:
    print(a)