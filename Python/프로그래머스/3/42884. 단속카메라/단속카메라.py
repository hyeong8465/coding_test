"""
21:52 -> 20:19

모든 차량이 한 번ㅇ느 단속 카메라를 만나도록 하려면 최소 몇 대의 카메라가 필요?

1. 정렬
2. 리스트 가장 앞에 있는 차량의 출구를 기준으로 잡는다.
3. 다음 차량이 해당 지점을 통과하는지 확인
    1. 다음 차량의 시작이 기준보다 앞이고,
        1. 끝이 기준보다 뒤면 기준 유지
        2. 끝이 기준보다 앞이면 기준을 끝으로 갱신
        3. 끝이 기준과 같으면 기준 유지
    2. 다음 차량의 시작이 기준보다 뒤면, 기준을 끝으로 갱신
    3. 기준과 같으면 기준 유지





엣지 케이스
한 구간이 다른 구간에 아예 속하는 경우


"""

def solution(routes):
    answer = 0
    cam = -30001
    routes.sort(key = lambda x: (x[0], x[1]))
    for start, end in routes:
        if start < cam and end < cam:
            cam = end
        elif start > cam:
            answer += 1
            cam = end
    return answer