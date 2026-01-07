import sys
input = sys.stdin.readline

def solve():
    R, C, M = map(int, input().split())
    
    # 상어 정보 저장 (딕셔너리 사용)
    # Key: (r, c), Value: (s, d, z)
    sharks = {}
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        # 좌표 0-index로 변환
        sharks[(r-1, c-1)] = (s, d, z)

    # 상, 하, 우, 좌 (문제의 d는 1,2,3,4 순서)
    # 0:위, 1:아래, 2:오른쪽, 3:왼쪽 으로 변환하여 사용하면 편함
    # 입력 d 변환: 1->0(위), 2->1(아래), 3->2(오른쪽), 4->3(왼쪽)
    
    # 방향 매핑 테이블 (입력 d -> 나의 d)
    # 위(1)->0, 아래(2)->1, 오른쪽(3)->2, 왼쪽(4)->3
    # 이를 처리하기 위한 리스트는 필요 없고, 입력 받을 때 처리하거나 함수 안에서 처리
    
    total_size = 0

    # 1. 낚시왕 이동 (0 ~ C-1)
    for fisher in range(C):
        # 2. 상어 잡기
        for r in range(R):
            if (r, fisher) in sharks:
                total_size += sharks[(r, fisher)][2]
                del sharks[(r, fisher)]
                break
        
        # 3. 상어 이동
        new_sharks = {}
        for (r, c), (s, d, z) in sharks.items():
            # 이동 로직 (수식 계산)
            nr, nc, nd = r, c, d
            
            # 위(1), 아래(2) 인 경우 -> 행 이동
            if d == 1 or d == 2:
                cycle = (R - 1) * 2
                if cycle == 0: # R이 1인 경우 제자리
                    dist = 0
                else:
                    dist = s % cycle
                
                # 방향 처리: d=1(위)는 index 감소, d=2(아래)는 index 증가
                # 계산 편의를 위해 1차원 직선상의 움직임으로 변환
                step = -1 if d == 1 else 1
                
                # 현재 위치에서 이동
                nr += step * dist
                
                # 경계 처리 (왕복 로직)
                while not (0 <= nr < R):
                    if nr < 0:
                        nr = -nr # 0 라인 대칭
                        nd = 2 # 아래로 변경
                    elif nr >= R:
                        nr = (R - 1) * 2 - nr # R-1 라인 대칭
                        nd = 1 # 위로 변경
            
            # 오른쪽(3), 왼쪽(4) 인 경우 -> 열 이동
            else:
                cycle = (C - 1) * 2
                if cycle == 0:
                    dist = 0
                else:
                    dist = s % cycle
                
                step = -1 if d == 4 else 1
                nc += step * dist
                
                while not (0 <= nc < C):
                    if nc < 0:
                        nc = -nc
                        nd = 3 # 오른쪽으로
                    elif nc >= C:
                        nc = (C - 1) * 2 - nc
                        nd = 4 # 왼쪽으로

            # 4. 잡아먹기 (딕셔너리에 넣을 때 크기 비교)
            if (nr, nc) in new_sharks:
                if new_sharks[(nr, nc)][2] < z:
                    new_sharks[(nr, nc)] = (s, nd, z)
            else:
                new_sharks[(nr, nc)] = (s, nd, z)
        
        sharks = new_sharks

    print(total_size)

if __name__ == "__main__":
    solve()