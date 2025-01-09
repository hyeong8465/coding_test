from itertools import permutations
a, b = input().split()
ans = -1
arr = []
for i in a:
  arr.append(i)

for p in permutations(a, len(a)):
  str = ""
  for i in p:
    str += i
  if str[0] == "0":
    continue
  else:
    temp = int(str)
    if temp < int(b):
      ans = max(ans, temp)
print(ans)