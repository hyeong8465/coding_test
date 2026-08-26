"""
13:47

가로, 세로 각각의 최댓값을 구해야 함
명함은 회전 가능

1. 전체 순회로 가로, 세로 최댓값 찾음
2. 가로, 세로 최댓값인 명함을 회전해서 값이 달라지는 지 확인
"""


def solution(sizes):
    max_x = 0
    max_y = 0
    
    for x, y in sizes:
        maxi = max(x, y)
        mini = min(x, y)
        
        max_x = max(maxi, max_x)
        max_y = max(mini, max_y)
    return max_x*max_y