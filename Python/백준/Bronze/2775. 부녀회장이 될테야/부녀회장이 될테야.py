T = int(input())

total = []
floor0 = list(range(1, 15))
total.append(floor0)
for f in range(0,14):
    temp = []
    for r in range(0,14):
        temp.append(sum(total[f][:r+1]))
    total.append(temp)

for i in range(T):
    f = int(input())
    r = int(input())
    print(total[f][r-1])