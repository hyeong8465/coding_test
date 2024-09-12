import sys
input = sys.stdin.readline

a = input().rstrip()
count = 0
for i in range(len(a)):
    try:
        if a[i] != a[i+1]:
            count += 1
    except:
        pass
if count%2 == 0:
    print(int(count/2))
else:
    print(int(count//2+1))