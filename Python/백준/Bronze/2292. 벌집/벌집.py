end = int(input())

cnt = 0
val = 1
for i in range(0,1000000000):
        val += i*6
        cnt += 1
        if end <= val:
            print(cnt)
            break
