from collections import deque
n, k = map(int, input().split())
arr = deque(range(1,n+1))

res = []
while arr:
    arr.rotate(-k+1)
    res.append(arr.popleft())
print('<'+', '.join(map(str, res))+ '>')