"""
다리를 여러번 건너도 도달할 수 있으면 통행 가능

가중치가 있는 최소거리

1. Dfs로 모든 경로를 완전 탐색 -> 불가능 O(N^(N-2))
2. 다익스트라 -> 다익스트라는 최단 경로 알고리즘임
3. MST

"""
def solution(n, costs):
    answer = 0

    parent = list(range(n))

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x,y):
        parent_x = find(x)
        parent_y = find(y)
        if parent_x < parent_y:
            parent[parent_y] = parent_x
        else:
            parent[parent_x] = parent_y

    costs.sort(key = lambda x: x[2])
    for start, end, cost in costs:

        # 사이클 체크
        if find(start) == find(end):
            continue

        union(start, end)
        answer += cost

    print(cost)
    return answer