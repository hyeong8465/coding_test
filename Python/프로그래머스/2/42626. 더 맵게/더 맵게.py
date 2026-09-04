"""
09:34 -> 9:47

모든 음식의 스코빌을 K 이상

음식 갯수: 최대 백만
heaq
"""
import heapq




def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville and scoville[0] < K:
        first = heapq.heappop(scoville)
        if scoville:
            second = heapq.heappop(scoville)
        else:
            return -1

        next = first+2*second
        heapq.heappush(scoville, next)
        answer += 1

    return answer