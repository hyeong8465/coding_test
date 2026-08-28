"""
15:21

전선 하나를 끊어서 두 개의 네트워크로 만들거임
각 네트워크에 속한 송전탑 갯수가 비슷하도록

완전 탐색
1. 끊을 와이어 하나 선택
2. 탐색으로 두 네트워크의 크기 찾음
"""


def solution(n, wires):
    answer = float("inf")

    # graph 생성
    graph = [[] for _ in range(n+1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)

    # dfs 정의
    def dfs(start, target_start, target_end, cnt):
        for end in graph[start]:
            if not visited[end]:
                if (start, end) in [(target_start, target_end), (target_end, target_start)]:
                    continue
                visited[end] = True
                cnt = max(cnt, dfs(end, target_start, target_end, cnt+1))
        return cnt

    for target_start, target_end in wires:
        # print(111, target_start, target_end)
        visited = [False]*(n+1)

        visited[1] = True
        temp = dfs(1, target_start, target_end, 1)
        # print(temp, n-temp)
        answer = min(answer, abs(n-temp - temp))
    # print(answer)
    return answer
