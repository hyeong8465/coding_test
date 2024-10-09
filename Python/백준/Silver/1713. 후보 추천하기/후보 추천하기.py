import sys

input = sys.stdin.readline

n = int(input())
students = int(input())
recommend_arr = list(map(int, input().split()))

window = []
time = 0
for i in recommend_arr:
    time += 1
    if i not in [j[0] for j in window]:
        if len(window) < n:
            rec = 1
            window.append([i,rec,time])
        else:
            window.sort(key = lambda x: (-x[1],-x[2]))
            window[-1][0] = i
            window[-1][1] = 1
            window[-1][2] = time
            # print(window)
    else:
        for w in window:
            if w[0] == i:
                w[1] = w[1]+1
    # print(window)
answer = [w[0] for w in window]
answer.sort()
print(*answer)