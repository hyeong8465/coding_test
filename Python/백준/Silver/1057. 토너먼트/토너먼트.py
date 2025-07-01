"""
10:22
완전 탐색

토너먼트 진행 - 홀수면 마지막 번호 부전승

임한수와 김지민이 만나기 전까진 계속 승리
각 번호가 주어질때 몇라운드에서 대결?

16 8 4 2
10만명
logN 번 경기 * N번 비교
17번

1,2,3,4,5,6
1 3 5



"""
n, a, b = map(int, input().split())

arr = list(range(n))
arr[a-1] = 'a'
arr[b-1] = 'b'

round = 0
while len(arr) >= 2:
    round += 1
    temp = []
    # print(len(arr))
    for idx in range(0, len(arr)-1, 2):
        # print(idx)
        if arr[idx] in ('a','b'):
            if arr[idx+1] in ('a','b'):
                print(round)
                quit()
            else:
                temp.append(arr[idx])
        elif arr[idx+1] in ('a', 'b'):
            temp.append(arr[idx+1])
        else:
            temp.append(arr[idx])
    if len(arr) % 2 != 0:
        temp.append(arr[-1])
    arr = temp
    # print(arr)
    # print(round)
print(-1)









