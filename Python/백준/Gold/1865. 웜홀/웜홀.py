import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline
# 충분히 큰 값을 무한대로 사용
INF = float('inf')

def solve():
    """
    각 테스트 케이스를 해결하는 함수
    """
    # N: 지점의 수, M: 도로의 개수, W: 웜홀의 개수
    N, M, W = map(int, input().split())

    # 간선 정보를 담을 리스트
    edges = []

    # 도로 정보 입력 (양방향)
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    # 웜홀 정보 입력 (단방향, 시간 감소는 음의 가중치로)
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    # 벨만-포드 알고리즘
    # 거리 배열을 0으로 초기화
    distance = [0] * (N + 1)

    # N번 반복
    for i in range(1, N + 1):
        # 모든 간선에 대해 완화(relaxation) 작업 수행
        for s, e, t in edges:
            # 현재 간선을 거쳐 가는 것이 더 짧은 경로라면 거리 갱신
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t

                # 만약 N번째 반복에서도 거리가 갱신된다면, 음수 사이클이 존재함
                if i == N:
                    return "YES"

    # N번의 반복 후에도 갱신이 발생하지 않았다면, 음수 사이클이 없음
    return "NO"

TC = int(input())
for _ in range(TC):
    result = solve()
    print(result)