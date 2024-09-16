import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    i, j = input().rstrip().split()
    dic[i] = j
for _ in range(M):
    i = input().rstrip()
    print(dic[i])