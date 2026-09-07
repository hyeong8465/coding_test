"""
13:13

경기 결과를 바탕으로 순위를 매기려 함
하지만 몇개 분실.
정확하게 순위를 매길 수 있는 선수의 수?

단방향 그래프
dfs로 연결된 네트워크 수 업데이트


"""

def solution(n, results):
    graph_win_to_lose = [[] for _ in range(n+1)]
    graph_lose_to_win = [[] for _ in range(n+1)]
    for win, lose in results:
        graph_win_to_lose[win].append(lose)
        graph_lose_to_win[lose].append(win)

    def dfs(start, graph, visited):
        for next in graph[start]:
            if next not in visited:
                visited.add(next)
                dfs(next, graph, visited)

    answer = 0
    for i in range(1, n+1):
        temp = 0
        visited = set()
        dfs(i, graph_win_to_lose, visited)
        temp += len(visited)

        visited = set()
        dfs(i, graph_lose_to_win, visited)
        temp += len(visited)

        if temp == n-1:
            answer += 1
            print(i)

    return answer