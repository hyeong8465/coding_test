import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0)
    quit()

vote = []
for _ in range(N):
    vote.append(int(input()))
dic = {}
dic[1] = vote[0]
dic[2] = vote[1:]
count = 0
while dic[1] <= max(dic[2]):
    dic[1] += 1 
    dic[2][dic[2].index(max(dic[2]))] -= 1
    count += 1
print(count)