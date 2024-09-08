N = int(input()) # 통화 수
arr = list(map(int, input().split()))
price1 = 0
for i in arr:
    if i % 30 != 0:
        price1 += (i//30 + 1)*10
    else:
        price1 += (i//30 + 1) * 10
price2 = 0
for i in arr:
    if i % 60 != 0:
        price2 += (i//60 + 1)*15
    else:
        price2 += (i//60+1) * 15
if price1 == price2:
    print(f"Y M {price1}")
elif price1 > price2:
    print(f"M {price2}")
else:
    print(f"Y {price1}")