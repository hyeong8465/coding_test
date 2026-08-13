"""
14:35
기능 개발 완료 순서는 상관없음
배포되어야 하는 순서는 있음
각 배포마다 몇 개의 기능이 배포되는가?

작업의 개수는 100개 이하

매일 speed 만큼 progress를 올림
가장 앞에 있는 작업의 progress가 100이상이 되면, 그 작업부터 progress가 100 이상인 작업 popleft

시간복잡도: 최대 100일 x (작업의 갯수 100개 + progress 체크 최대 100개)
러프하게 생각했을 때 100^3 = 1000000
시간 넉넉
deque로 앞에서부터 아예 빼버리면 반복문마다 작업의 갯수를 줄일 수 있음

"""
from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                continue
            progresses[i] += speeds[i]
        
        temp = 0
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            temp += 1
        if temp != 0:
            answer.append(temp)
    
    return answer