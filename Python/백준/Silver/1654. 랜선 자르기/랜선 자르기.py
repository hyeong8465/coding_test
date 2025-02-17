"""
서로 다른 길이의 K 개의 랜선을 N개의 같은 길이의 랜선으로 만들고 싶음
만들 수 있는 최대 랜선의 길이
"""
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

result = 0
start = 1
end = max(arr)
answer = 0
while start <= end:
    mid = (start+end)//2
    # 자른 랜선 수 저장
    result = sum(a // mid for a in arr)

    # print(mid, result)
    
    if result >= n:
        answer = mid
        start = mid+1
    else:
        end = mid - 1
print(answer)
