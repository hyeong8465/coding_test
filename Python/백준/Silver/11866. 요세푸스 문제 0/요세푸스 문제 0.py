"""
N: 1000
리스트 사용시 삭제 O(N)
O(N^2)의 시간 복잡도

큐


"""
from collections import deque
n, k = map(int, input().split())
arr = deque(range(1,n+1))

res = []
while arr:
    arr.rotate(-k+1)
    res.append(arr.popleft())
print('<'+', '.join(map(str, res))+ '>')


    

