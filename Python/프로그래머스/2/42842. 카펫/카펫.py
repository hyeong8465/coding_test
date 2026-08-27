"""
14:27 -> 14:36

전체 카펫의 크기는 모르지만, 노란색, 갈색 격자의 갯수는 기억함
카펫의 가로 세로 크기는?

완전 탐색
1. yellow의 약수를 가로, 세로로 설정
2. 테두리의 크기가 brown 값과 같은지 확인
3. 테두리 확정. 가로 길이가 세로보다 같거나 길게

제한사항
yellow는 최대 200만
O(N)
"""
def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        if yellow%i == 0:
            row = i
            col = yellow//i
            if 2*((row+2)+col) == brown:
                r = row+2
                c = col+2
                answer.append(max(r,c))
                answer.append(min(r,c))
                return answer