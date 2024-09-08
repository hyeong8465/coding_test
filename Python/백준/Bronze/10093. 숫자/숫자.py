arr = list(map(int, input().split()))
arr.sort()
a, b = arr[0], arr[1]
if a == b:
    print(0)
    print("")
else:
    print(b-a-1)
    for i in range(a+1,b):
        print(i, end=" ")