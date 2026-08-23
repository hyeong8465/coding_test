"""
16:55

n = words 리스트의 길이
l = 각 단어의 길이
1. 이동할 수 있는 조합 찾아서 인접리스트 만들기 -> O(N^2*l)
    len(set(a) - set(b)) == 1 확인
    abbc -> a,b,c
    abcc -> a,b,c

2. 인접 리스트에서 bfs 시작 -> O(N)
"""
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # 1. 인접리스트 만들기
    words = [begin]+words # 비효율적인 것 같은데 다른 방법이 안떠오름
    n = len(words)
    graph = [[] for _ in range(n)] # 0번째는 begin
    for i in range(n):
        word_1 = words[i]
        for j in range(i+1,n):
            word_2 = words[j]
            cnt = 0
            for w_1, w_2 in zip(word_1, word_2):
                if w_1 != w_2: cnt += 1
                if cnt > 1: break
            # print(word_1, word_2, cnt)
            if cnt == 1:
                graph[i].append(j)
                graph[j].append(i)
    # print(graph)
    
    # bfs
    q = deque([(0,0)])
    visited = [False]*n
    visited[0] = True
    
    while q:
        i,cnt = q.popleft()
        if words[i] == target:
            return cnt
        for ni in graph[i]:
            if not visited[ni]:
                q.append((ni,cnt+1))
                visited[ni] = True
        