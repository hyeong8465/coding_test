"""
16:31
모든 트럭이 다리를 건너는데 걸리는 최소 시간
대수, 무게 제한 있음
다리에 완전히 올라야 트럭의 무게가 다리에 실림

O(브릿지 길이 * 트럭 수)


"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()  # (트럭 무게, 다리를 완전히 벗어나는 시각)
    time = 0
    load = 0

    for w in truck_weights:
        time += 1  # 한 스텝에 트럭 한 대만 올라탐
        while q and q[0][1] <= time:
            ew, _ = q.popleft()
            load -= ew
        while load + w > weight:
            ew, et = q.popleft()
            load -= ew
            time = et
        q.append((w, time + bridge_length))
        load += w

    return q[-1][1]