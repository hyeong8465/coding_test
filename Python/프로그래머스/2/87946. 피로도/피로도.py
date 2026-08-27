"""
14:50 -> 15:18

최소 필요 피로도
소모 피로도

탐험할 수 있는 최대 던전 수

DFS로 완전 탐색 -> O(N^2) -> O(64)

"""


def solution(k, dungeons):
    global answer
    answer = 0
    n = len(dungeons)
    visited = [False]*n

    def dfs(now, cnt):
        global answer
        for i in range(n):
            minimum = dungeons[i][0]
            using = dungeons[i][1]
            if visited[i]:
                continue
            if now >= minimum:
                visited[i] = True
                answer = max(answer, cnt+1)
                dfs(now-using, cnt+1)
                visited[i] = False

    dfs(k, 0)
    print(answer)
    return answer