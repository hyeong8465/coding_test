import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

stack = []
stack.append(arr)
cnt_w = 0
cnt_b = 0
cnt = 0
while stack:
    s_t = stack.pop()
    cnt+=1
    # print(cnt, '==================')
    # for i in s_t:
    #     print(i)
    
    val = 0
    for i in s_t:
        val += sum(i)
    if val == 0:
        cnt_w += 1
    elif len(s_t)**2 == val:
        cnt_b += 1
    else:
        n_t = int(len(s_t)/2)
        stack.append([i[:n_t] for i in s_t[:n_t]]) # 1
        stack.append([i[n_t:] for i in s_t[:n_t]]) # 2
        stack.append([i[:n_t] for i in s_t[n_t:]]) # 3
        stack.append([i[n_t:] for i in s_t[n_t:]]) # 4
    # print(cnt_b, cnt_w)
print(cnt_w)
print(cnt_b)

        

    
    