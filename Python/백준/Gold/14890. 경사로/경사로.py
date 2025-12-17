n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check_line(line):
    used = [False]*n
    
    for i in range(n-1):
        if line[i] == line[i+1]:
            continue

        if abs(line[i]-line[i+1]) > 1:
            return False
        
        if line[i] > line[i+1]: # 내리막
            temp = line[i+1]
            for j in range(i+1, i+1+l):
                if 0<=j<n:
                    if line[j] != temp or used[j]:
                        return False
                    used[j]=True
                else:
                    return False
        else: # 오르막
            temp = line[i]
            for j in range(i, i-l, -1):
                if 0 <=j<n:
                    if line[j] != temp or used[j]:
                        return False
                    used[j] = True
                else:
                    return False
    return True

ans = 0
# 행 기준
for row in graph:
    if check_line(row):
        ans += 1


for col in zip(*graph):
    if check_line(col):
        ans += 1

print(ans)