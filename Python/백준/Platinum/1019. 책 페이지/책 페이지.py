"""
n이 10억이라 완전 탐색으론 못 풂 O(N^2)


"""



# n = int(input())




"""
n = 1 ; 0 1 0 0 0 ...
n = 2 ; 0 1 1 0 0 ...
...
n = 9 ; 
n = 10 ; 1
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20


"""
n = input()
if len(n) == 1:
    print('0', end=' ')
    for i in range(9):
        if i+1 <= int(n):
            print('1', end = ' ')
        else:
            print('0', end = ' ')
    quit()

pos = 0
ans = 0
# for i in range(1,len(n)):
#     if int(n[i]) == 0:
#         a = int(n[:i])*(int(n[i+1:])+1)
#     else:
#         a = int(n[:i])*10**(len(n)-i-1)
#     print(a)
#     ans += a
# print(ans, end = ' ')

for i in range(1, len(n)):   
    left_part = int(n[:i])  # n의 앞 부분 (최소 1자리)
    right_part = int(n[i+1:]) if i + 1 < len(n) else 0  # n[i+1:]이 빈 문자열이면 0으로 처리

    if int(n[i]) == 0:
        a = (left_part-1) * 10**(len(n) - i - 1)  # 0을 처리하는 경우
        a += right_part+1
    else:
        a = left_part * 10**(len(n) - i - 1)  # 일반적인 경우

    # print(a)
    ans += a
print(ans, end=' ')

    
for pos in range(1,10):
    ans = 0
    for i in range(len(n)):
        if int(n[i]) > pos: # 인덱스 뒤는 99여도 됨
            a = n[:i]+'9'*(len(n)-i-1)
            # print(1)
        elif int(n[i]) == pos:
            a = n[:i]+n[i+1:]
        else:
            if i == 0:
                continue
            else:
                a = str(int(n[:i])-1)+'9'*(len(n)-i-1)
        # print(a)
        ans += int(a)+1
    print(ans, end = ' ')