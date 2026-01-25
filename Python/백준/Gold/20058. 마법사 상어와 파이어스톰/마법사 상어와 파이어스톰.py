import sys
from collections import deque
input = sys.stdin.readline

# [최적화 1] 전체 로직을 함수 하나로 감싸서 '지역 변수'로 만듦
def solve():
    n, q = map(int, input().split())
    N_SIZE = 1 << n # 2**n과 동일 (취향 차이)
    ices = [list(map(int, input().split())) for _ in range(N_SIZE)]
    l_list = list(map(int, input().split()))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # BFS는 호출 횟수가 적으므로 함수로 분리해도 괜찮음 (내부 함수로 정의)
    def bfs(x, y, visited):
        cnt = 1
        q_bfs = deque([(x, y)])
        visited[x][y] = True

        while q_bfs:
            cx, cy = q_bfs.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < N_SIZE and 0 <= ny < N_SIZE:
                    if ices[nx][ny] != 0 and not visited[nx][ny]:
                        q_bfs.append((nx, ny))
                        visited[nx][ny] = True
                        cnt += 1
        return cnt

    for l in l_list:
        sub_size = 1 << l # 2**l
        
        # 1. 회전 (Rotate)
        # 0이면 회전할 필요 없음 (가지치기)
        if l > 0:
            for i in range(0, N_SIZE, sub_size):
                for j in range(0, N_SIZE, sub_size):
                    # 슬라이싱 + zip 활용 (작성하신 대로 잘 하셨습니다!)
                    submatrix = [row[j:j+sub_size] for row in ices[i:i+sub_size]]
                    rotated_sub_matrix = list(map(list, zip(*submatrix[::-1])))
                    
                    for idx in range(sub_size):
                        ices[i+idx][j:j+sub_size] = rotated_sub_matrix[idx]
        
        # 2. 얼음 녹이기 (Reduce)
        reduce_candidates = []
        
        # [최적화 2] is_reduce 함수 호출 제거 -> 코드 인라인(Inlining)
        # 함수 호출 오버헤드(400만 번)가 사라짐
        for i in range(N_SIZE):
            for j in range(N_SIZE):
                if ices[i][j] == 0: continue
                
                adj_cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N_SIZE and 0 <= ny < N_SIZE:
                        if ices[nx][ny] > 0:
                            adj_cnt += 1
                
                if adj_cnt < 3:
                    reduce_candidates.append((i, j))
        
        # 한꺼번에 녹이기
        for i, j in reduce_candidates:
            ices[i][j] -= 1

    # 3. 정답 출력
    ans_sum = sum(sum(row) for row in ices)
    print(ans_sum)

    ans_max = 0
    visited = [[False]*N_SIZE for _ in range(N_SIZE)]
    
    for i in range(N_SIZE):
        for j in range(N_SIZE):
            if not visited[i][j] and ices[i][j] != 0:
                ans_max = max(ans_max, bfs(i, j, visited))

    print(ans_max)

# 실행
solve()