import sys
input = sys.stdin.readline

n = int(input())
count = 0
for i in range(1, n+1):
    i_str = str(i)
    if len(i_str) == 1 or len(i_str) == 2:
        count += 1
    else:
        d = int(i_str[1]) - int(i_str[0])
        for j in range(len(i_str)-1):
            # print(i, d)
            if int(i_str[j+1]) - int(i_str[j]) != d:
                # print(int(i_str[j+1]) - int(i_str[j]) != d)
                break
            if j == len(i_str)-2:
                count += 1
print(count)