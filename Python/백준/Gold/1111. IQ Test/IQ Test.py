# try1:
n = int(input())
nums = list(map(int, input().split()))
if n == 1:
    print('A')
    quit()
if n == 2:
    if nums[0] == nums[1]:
        print(nums[0])
        quit()
    else:
        print('A')
        quit()


p1 = (nums[0], nums[1])
p2 = (nums[1], nums[2])

if nums[0] == nums[1]:
    a = 0
else:
    if (nums[2] - nums[1]) % (nums[1] - nums[0]) != 0:
        print('B')
        quit()
    a = (p1[1]-p2[1])//(p1[0]-p2[0])
b = p1[1]-p1[0]*a
# print(a, b)

for i in range(1,n):
    if nums[i] != a*nums[i-1]+b:
        print('B')
        quit()

print(int(a*nums[-1]+b))