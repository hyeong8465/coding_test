"""
i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화

"""
n,m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)

result = 0
while start <= end:
    mid = (start+end)//2
    
    cnt = 1
    temp = 0
    for a in arr:
        temp += a
        if temp > mid:
            cnt += 1
            temp = a
    # print(cnt)
    if cnt > m: # 용량이 부족해서 cnt가 많음
        start = mid+1 # 용량을 늘림
    else: # 용량이 넉넉해서 cnt가 m보다 적거나 같음
        result = mid
        end = mid-1 # 용량 줄이기
    # print(mid)        
print(result)






