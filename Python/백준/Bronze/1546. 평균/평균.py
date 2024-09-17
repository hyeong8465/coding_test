import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

val_max = max(arr)
new_arr = [x/val_max*100 for x in arr]
print(sum(new_arr)/n)