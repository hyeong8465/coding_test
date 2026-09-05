"""
15:14


- 큐에 숫자 삽입
    - 최소 힙, 최대 힙 모두에 (숫자, id) 삽입
- 큐에 최댓값 삭제
    1. id가 set에 있거나 list[id] == True 이면, 조건을 만족하지 않을 때까지 pop
- 큐에 최솟값 삭제
    1. id가 set에 있거나 list[id] == True 이면, 조건을 만족하지 않을 때까지 pop

1. 최소 힙
2. 최대 힙
3. 상태 관리 -> set? list?

N = 100만
시간복잡도: O(NlogN의 상수배)
공간복잡도: O(N)

"""
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    deleted_idx = set()

    for i, operation in enumerate(operations):
        op = list(operation.split(" "))
        if op[0] == "I":
            heapq.heappush(min_heap, (int(op[1]), i))
            heapq.heappush(max_heap, (-int(op[1]), i))
        else: # 삭제 연산
            if op[1] == "-1": # 최솟값 삭제
                while min_heap and min_heap[0][1] in deleted_idx:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    deleted_idx.add(idx)
            else: # 최댓값 삭제
                while max_heap and max_heap[0][1] in deleted_idx:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    deleted_idx.add(idx)
        # print(i)
        # print(min_heap)
        # print(max_heap)

    min_val = 0
    max_val = 0

    while min_heap and min_heap[0][1] in deleted_idx:
        heapq.heappop(min_heap)
    while max_heap and max_heap[0][1] in deleted_idx:
        heapq.heappop(max_heap)

    if len(min_heap) == 1:
        return [min_heap[0][0], min_heap[0][0]]

    if min_heap:
        min_val, idx = heapq.heappop(min_heap)
        deleted_idx.add(idx)
    if max_heap:
        max_val, idx = heapq.heappop(max_heap)
        deleted_idx.add(idx)

    return [-max_val, min_val]
