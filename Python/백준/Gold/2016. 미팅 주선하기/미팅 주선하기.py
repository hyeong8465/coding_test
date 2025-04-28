"""
시뮬레이션, 브루트포스?


1. 태현1 남2~5 여6~10
2. 각자 선호도 선택
3. 여학생이 선호도 순으로 프로포즈, 퇴짜를 놓은 남학생이라면 다음 순위에게 프로포즈
4. 짝이 없는 남학생은 무조건 받음, 짝이 있으면 자신을 더 좋아하는 여학생 선택
5. 퇴짜 받은 여학생만 다음 라운드 참여
6. 모두 짝을 찾을 때까지 반복

다른 사람의 선호도를 알고 있을 때, 원래 짝보다 더 좋아하는 여학생과 매칭 가능?
"""
from itertools import permutations
import sys
input = sys.stdin.readline
t = int(input())

def partner(likes):
    likes = [l[:] for l in likes]
    partners = [[] for _ in range(6)] # 인덱스는 남자번호, 내용은 여자번호
    # print(partners)

    # 여학생의 선택
    for i in range(6,11):
        partners[likes[i][0]].append(i)
    # print(0000, partners)
    
    while True:
        canceled = []
        # 남학생의 선택
        for i in range(1,6):
            if len(partners[i]) >= 2:
                p = partners[i][0]
                idx = likes[i].index(p) # 첫번째 파트너의 선호도
                for partner in partners[i]: # 다른 파트너의 선호도와 비교해서 업데이트
                    temp_idx = likes[i].index(partner)
                    if temp_idx < idx:
                        canceled.append(p)
                        p = partner
                        idx = temp_idx
                    elif temp_idx > idx:
                        canceled.append(partner)
                partners[i] = [p] # 파트너는 한명으로 업데이트
        # print(1111, partners)
        # print(1111, canceled)
        
        # 종료 조건
        if len(canceled) == 0:
            break

        # 다음 라운드
        for i in range(len(canceled)):
            girl = canceled[i]  
            likes[girl].pop(0)
            partners[likes[girl][0]].append(girl)
            # print(partners)
        # print(2222, partners)
    return partners[1]
            

for _ in range(t):
    flag = False
    likes = [[],[6,7,8,9,10]]
    for _ in range(9):
        temp = list(map(int, input().split()))
        likes.append(temp)
    init = partner(likes)
    # print(init)
    for i in permutations(range(6,11), 5):
        likes[1] = list(i)
        # print(likes[1])
        res = partner(likes)
        # print(res)
        if res < init:
            flag = True
            break
    if flag:
        print('YES')
    else:
        print('NO')


    
    
    

            

"""
1
10 9 6 7 8
8 10 7 9 6
9 7 6 8 10
8 10 6 9 7
2 3 1 4 5
5 1 2 3 4
3 2 1 4 5
2 3 1 5 4
5 3 4 1 2

"""






