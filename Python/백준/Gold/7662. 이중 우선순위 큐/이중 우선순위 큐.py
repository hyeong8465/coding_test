import sys
import heapq

input = sys.stdin.readline

def sync(heap, erased):
    """ 힙에서 삭제된 값들을 정리하는 함수 """
    while heap and erased[heap[0][1]] > 0:
        _, index = heapq.heappop(heap)
        erased[index] -= 1  # 삭제 처리

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    k = int(input())  # 연산 개수
    min_heap = []  # 최소 힙 (최솟값 추출용)
    max_heap = []  # 최대 힙 (최댓값 추출용, 음수로 저장)
    erased = {}  # 삭제된 노드 관리

    for i in range(k):
        cmd, num = input().split()
        num = int(num)

        if cmd == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            erased[i] = 0  # 삭제 여부 초기화

        elif cmd == "D":
            if num == 1:  # 최댓값 삭제
                sync(max_heap, erased)
                if max_heap:
                    erased[max_heap[0][1]] += 1
                    heapq.heappop(max_heap)

            elif num == -1:  # 최솟값 삭제
                sync(min_heap, erased)
                if min_heap:
                    erased[min_heap[0][1]] += 1
                    heapq.heappop(min_heap)

    # 최종 결과 정리 (동기화)
    sync(min_heap, erased)
    sync(max_heap, erased)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])  # 최댓값, 최솟값 출력
    else:
        print("EMPTY")  # 비어 있는 경우