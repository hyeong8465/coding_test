"""
13:16

각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리로 구성
코스요리에는 최소 2개 이상의 단품 메뉴
최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합만 사용

구현

문자열도 정렬, 리스트도 정렬
메뉴 구성이 여러 개라면, 모두 배열에 담아 return

1. orders를 순회하면서, 단품 메뉴 count
    count가 2미만인 메뉴 확인
2. 각 order의 course의 수만큼의 길이를 갖는 조합을 만들어서 해당 조합 자체를 count
3. 각 길이마다 가장 많이 나온 조합을 찾고, 조건 1에 속하면 pass


"""
from itertools import combinations


def solution(orders, course):
    # 각 알파벳 카운트
    str_list = {}
    for o in orders:
        for i in list(o):
            if i in str_list:
                str_list[i] += 1
            else:
                str_list[i] = 1
    # 2회 미만인 알파벳 저장
    del_list = set()
    for k, v in str_list.items():
        if v < 2:
            del_list.add(k)
        
    # print(del_list)

    norders = []
    for o in orders:
        temp = []
        for i in list(o):
            if i in del_list:
                continue
            else:
                temp.append(i)
        temp.sort()
        norders.append(temp)
    orders = norders

    # print(orders)

    # 각 조합의 갯수 저장
    comb_list = []
    for c in course:
        temp = {}
        for o in orders:
            for t in list(combinations(list(o), c)):
                if t in temp:
                    temp[t] += 1
                else:
                    temp[t] = 1
        comb_list.append(temp)
    
    # print(comb_list)
    
    answer = []

    for comb in comb_list:
        temp = [(k,v) for k,v in comb.items()]
        temp.sort(key = lambda x: -x[1])
        
        if len(temp) > 0:
            if temp[0][1] < 2:
                continue
            
            answer.append(''.join(temp[0][0]))

            for i in range(len(temp)-1):
                if temp[i][1] == temp[i+1][1]:
                    answer.append(''.join(temp[i+1][0]))
                else:
                    break
    answer.sort()
    # print(answer)
    return answer

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]

solution(orders, course)