from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # 1. 각 코스 요리 길이(c)마다 반복
    for c in course:
        menu_combos = []
        
        # 2. 모든 주문에 대해 c개의 메뉴 조합 생성
        for order in orders:
            # [핵심] "XW"와 "WX"가 같은 조합으로 취급되도록 미리 정렬
            for combo in combinations(sorted(order), c):
                menu_combos.append(combo)
                
        # 3. Counter를 이용해 각 조합의 등장 횟수를 자동으로 계산
        counter = Counter(menu_combos)
        
        # 4. 조합이 하나라도 만들어졌다면 가장 많이 나온 조합 찾기
        if counter:
            # most_common(1)은 가장 빈도가 높은 1개를 리스트 안의 튜플로 반환
            # 예: [(('A', 'C'), 4)] -> [0][1]을 하면 최대 빈도수인 4가 나옴
            max_count = counter.most_common(1)[0][1]
            
            # 최소 2명 이상 주문한 경우에만 정답 후보에 포함
            if max_count >= 2:
                for menu, count in counter.most_common():
                    if count == max_count:
                        # 튜플 ('A', 'C')를 문자열 'AC'로 합쳐서 추가
                        answer.append(''.join(menu))
                    else:
                        break # 빈도수가 낮아지면 더 볼 필요 없이 중단
                        
    # 5. 최종 결과를 알파벳 오름차순으로 정렬
    return sorted(answer)