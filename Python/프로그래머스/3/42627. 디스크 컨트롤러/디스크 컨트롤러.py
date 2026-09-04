"""
10:17

번호, 요청시각, 소요시간

소요시간, 요청시각, 번호 순으로 우선순위가 있음

시뮬?
1. 1초씩 시간을 늘림
2. jobs을 정렬 후500log500, 현재 시각에 맞는 일을 큐에 넣음 500log500
3. 작업시간이 끝나면 큐에서 1개 빼서 처리 logN
최악의 경우 1000초 걸리는 500개의 작업이 1000초에 들어와도 1000+500*1000 = 501000
50.1만번 반복이 heap보다 압도적


* 50.1만 초를 모두 시뮬레이션 하지 않고 의미있는 시간으로 바로 점프한다.
"""
import heapq

def solution(jobs):
    jobs.sort()

    n = len(jobs)
    answer = 0
    idx = 0
    q = []
    time = 0

    while idx < n or q:
        while idx < n and jobs[idx][0] <= time:
            start, duration = jobs[idx]
            heapq.heappush(q, (duration, start, idx))
            idx += 1


        if q:
            duration, start, i  = heapq.heappop(q)
            time += duration
            answer += time - start
        else:
            time = jobs[idx][0]
    return answer//n