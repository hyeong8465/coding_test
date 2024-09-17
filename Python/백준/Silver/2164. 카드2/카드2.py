import sys
from collections import deque

input = sys.stdin.readline

arr = deque(range(1, int(input())+1))
while True:
    if len(arr) == 1:
        print(arr[0])
        break
    else:
        arr.popleft()
        arr.append(arr.popleft())