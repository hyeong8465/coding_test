import sys
#sys.setrecursionlimit(2000)

dice = list(map(int, input().split()))

# 1. 맵 연결 구조 정의 (이전과 동일)
# 0~20: 메인 경로, 21: 도착, 22~: 파란 경로
adj = [i+1 for i in range(33)]
adj[20] = 21 # 40 -> 도착
adj[21] = 21 # 도착 -> 도착 (이동 멈춤)

# 분기점 연결
adj[24] = 25 # 19 -> 25
adj[25] = 26 # 25 -> 30
adj[26] = 27 # 30 -> 35
adj[27] = 20 # 35 -> 40

adj[29] = 25 # 24 -> 25
adj[32] = 25 # 26 -> 25

# 파란 화살표 시작점 매핑
blue_start = {
    5: 22,  # 10 -> 13
    10: 28, # 20 -> 22
    15: 30  # 30 -> 28
}

# 2. [핵심] 점프 테이블 미리 계산 (Pre-calculation)
# jumps[start_node][steps] : start_node에서 steps만큼 갔을 때 도착 위치
# 최대 주사위 눈금은 5
jumps = [[0] * 6 for _ in range(33)]

for i in range(33):
    curr = i
    for step in range(6): # 0칸~5칸 이동 결과 저장
        jumps[i][step] = curr
        if curr == 21: # 도착점에 있다면 계속 도착점
            curr = 21
        else:
            curr = adj[curr]

# 점수판
score_board = [0] * 33
for i in range(21): score_board[i] = i * 2
score_board[22], score_board[23], score_board[24] = 13, 16, 19
score_board[25], score_board[26], score_board[27] = 25, 30, 35
score_board[28], score_board[29] = 22, 24
score_board[30], score_board[31], score_board[32] = 28, 27, 26
score_board[21] = 0

horses = [0, 0, 0, 0]
max_score = 0

def dfs(turn, current_score):
    global max_score
    
    if turn == 10:
        max_score = max(max_score, current_score)
        return

    for i in range(4):
        curr = horses[i]
        
        # 도착한 말은 스킵
        if curr == 21:
            continue
            
        move = dice[turn]
        
        # [변경점] while 루프 대신 O(1) 조회
        if curr in blue_start:
            # 파란 화살표인 경우:
            # 첫 1칸은 파란 경로로 진입, 나머지(move-1)는 미리 계산된 테이블 사용
            start_blue = blue_start[curr]
            nxt = jumps[start_blue][move - 1]
        else:
            # 일반 경로: 테이블에서 바로 조회
            nxt = jumps[curr][move]
        
        # 도착 칸이 아닌데, 다른 말이 있으면 못감
        if nxt != 21 and nxt in horses:
            continue
            
        # 백트래킹
        original = horses[i]
        horses[i] = nxt
        
        dfs(turn + 1, current_score + score_board[nxt])
        
        horses[i] = original

dfs(0, 0)
print(max_score)