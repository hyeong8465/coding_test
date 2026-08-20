"""
23:06

인접행렬


"""
from collections import deque

def bfs(start, visited, n, computers):
    q = deque([start])
    visited[start] = True
    
    while q:
        x = q.popleft()
        for i, c in enumerate(computers[x]):
            if not visited[i] and c == 1:
                q.append(i)
                visited[i] = True
    return visited
    

def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited = bfs(i, visited, n, computers)
    return answer