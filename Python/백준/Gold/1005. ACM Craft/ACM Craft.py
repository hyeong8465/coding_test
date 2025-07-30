# try 2: 탑 다운 재귀
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


t = int(input())

def recursive(end):
    if dp[end] != -1:
        return dp[end]
    
    if len(graph[end]) == 0: # 시작점이면
        dp[end] = cost[end]
        return dp[end]
    
    ans = 0
    for start in graph[end]:
        ans = max(ans, recursive(start))
    
    dp[end] = ans + cost[end]
    return dp[end]
    
for _ in range(t):
    n, k = map(int, input().split())
    cost = [0]+ list(map(int, input().split()))
    
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        start, end = map(int, input().split())
        graph[end].append(start)
    
    w = int(input())

    dp = [-1]*(n+1)

    print(recursive(w))