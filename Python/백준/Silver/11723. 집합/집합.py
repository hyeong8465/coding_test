"""
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
"""
import sys
input = sys.stdin.readline
M = int(input())
answer = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0}
for _ in range(M):
    arr = list(input().split())
    if len(arr) == 2:
        a = arr[0]
        b = arr[1]
    else:
        a = arr[0]
    
    if a == 'check':
        if answer[b] == 1:
            print(1)
        else:
            print(0)
    elif a == 'add' and (answer[b] != 1):
        answer[b] = 1
    elif a == 'remove'and (answer[b] == 1):
        answer[b] = 0
    elif a == 'toggle':
        if answer[b] == 1:
            answer[b] = 0
        else:
            answer[b] = 1
    elif a == 'all':
        answer = {'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'10':1,'11':1,'12':1,'13':1,'14':1,'15':1,'16':1,'17':1,'18':1,'19':1,'20':1}
    elif a == 'empty':
        answer = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0}