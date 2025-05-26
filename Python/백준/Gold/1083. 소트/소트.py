"""
크기가 n인 배열, n: 50
배열에 담긴 수는 모두 다름
연속된 두 개의 원소만 교환 가능, 교환은 s번
사전순으로 가장 뒷서는 것을 출력 -> 오름차순 정렬
가장 큰 수를 최우선으로 앞으로

try1: 배열의 앞에서부터 길이 s만큼의 배열에서 최댓값을 찾고 그 값을 가장 앞으로 이동
O(S*N): 5천만
시간 제한: 2초
그리디, 정렬


"""
n = int(input())
arr = list(map(int, input().split()))
s = int(input())

idx = 0

# for _ in range(1):
while True:
    if idx == n-1: break # 모두 정렬되면 마무리
    if s == 0: break # s가 0이 되면 마무리

    # 길이 s만큼 배열에서 최대값 위치 찾음
    max_idx = 0
    max_val = 0
    for i in range(idx, min(n, idx+s+1)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i

    # print(max_idx)

    for i in range(max_idx, idx, -1):
        arr[i], arr[i-1] = arr[i-1], arr[i]
    # print(arr)
    s -= max_idx-idx
    idx += 1
print(*arr)

    
    
