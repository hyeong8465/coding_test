"""
09:54

1. 화살표 방향으로만 이동 가능, 파란 칸에서는 파란 색 화살표만 사용
    1. 이동 중이거나 파란색이 아닌 칸에서 출발하면 빨간색 화살표
    2. 도착칸에 이동하면 주사위 수랑 상관없이 이동 종료
2. 10개의 턴, 1-5 주사위, 말 하나를 골라 주사위 수만큼 이동
3. 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없음,
    단, 이동을 마치는 칸이 도착 칸이면 고를 수 있음
4. 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가

주사위가 나올 수 10개가 주어졌을 때, 얻을 수 있는 점수의 최댓값?

시뮬
백트래킹
브루트포스 O(4**10) -> 100만

for idx, route_idx in horses:
    temp_idx = horse+dice
    if route_idx == 0 and route[route_idx][temp_idx] in [10,20,30]:
        if route_idx
    
    
    
    temp_route_idx
    if (horse + dice,
    horse += dice
    

1. 아무 말이나 잡아서 dice의 값만큼 route에서 이동
    1. 해당 칸에 다른 말이 있으면 continue
    1. 이동한 위치의 값이 10, 20, 30에 속하면 route 업데이트


"""
# import sys
# sys.setrecursionlimit(10**9)

# dice = list(map(int, input().split()))

# horses = [(0,0) for _ in range(4)] # (index, route_index)

# route0 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
# route1 = [10,13,16,19,25,30,35,40]
# route2 = [20,22,24,25,30,35,40]
# route3 = [30,28,27,26,25,30,35,40]
# routes = [route0, route1, route2, route3]

# answer = 0
# def backtracking(cnt, score):
#     # 종료 조건
#     if cnt == 10:
#         global answer
#         answer = max(score, answer)
#         return
    
#     for i in range(4): # 4마리의 말
#         # 이동 가능한 말인지 체크
#         idx, route_idx = horses[i]
        
#         # 이미 도착한 말은 패스
#         if idx >= len(routes[route_idx]):
#             continue
        
#         temp_idx = idx+dice[cnt]        
        
#         if 0<=temp_idx<len(routes[route_idx]) and route_idx == 0 and routes[route_idx][temp_idx] in [10,20,30]:
#             temp = routes[route_idx][temp_idx]
            
#             if temp == 10:
#                 temp_route_idx = 1
#             elif temp == 20:
#                 temp_route_idx = 2
#             elif temp == 30:
#                 temp_route_idx = 3
#             else:
#                 temp_route_idx = 0
#             temp_idx = 0
#         else:
#             temp_route_idx = route_idx
        
#         # print(cnt, temp_idx, temp_route_idx)
#         # print(routes[temp_route_idx][temp_idx])
#         if (temp_idx, temp_route_idx) in horses: # 이동 불가
#             continue
        
#         # 이동
#         horses[i] = (temp_idx, temp_route_idx)

#         # 점수 합산
#         if 0<=temp_idx<len(routes[route_idx]):
#             score += routes[temp_route_idx][temp_idx]

#         # backtracking
#         backtracking(cnt+1, score)
#         horses[i] = (idx, route_idx)

# backtracking(0, 0)
# print(answer)

"""
10:58 GEMINI
문제 1. 공유 구간 처리 실패
    25,30,35,40 값은 모든 경로에서 같이 존재
    route1의 25 -> (4,1)
    route2의 25 -> (3,2)
    실제로는 같은 칸이라 이동할 수 없어야 하는데, 튜플이 다르므로 이동 가능하다고 판단 -> 로직 오류
=> 경로 표현 방식 변경

문제 2. 
    backtracking에 (cnt+1, score+획득점수) 형태로 전달해야 제대로 작동함

"""


import sys
sys.setrecursionlimit(2000)

# 주사위 입력
dice = list(map(int, input().split()))

# 다시 정리한 next_node 테이블
next_node = [i+1 for i in range(33)]
next_node[20] = 21 # 40 -> 도착
next_node[21] = 21 # 도착 -> 도착

# 10번 출발 합류
next_node[24] = 25 # 19 -> 25
next_node[25] = 26 # 25 -> 30
next_node[26] = 27 # 30 -> 35
next_node[27] = 20 # 35 -> 40

next_node[29] = 25 # 24 -> 25 (20번 출발 합류)
next_node[32] = 25 # 26 -> 25 (30번 출발 합류)

# 파란 화살표 (특별한 시작점)
blue = {}
blue[5] = 22  # 10 -> 13
blue[10] = 28 # 20 -> 22
blue[15] = 30 # 30 -> 28

# 점수판
score_board = [0] * 33
for i in range(21): score_board[i] = i * 2
score_board[22], score_board[23], score_board[24] = 13, 16, 19
score_board[25], score_board[26], score_board[27] = 25, 30, 35
score_board[28], score_board[29] = 22, 24
score_board[30], score_board[31], score_board[32] = 28, 27, 26
score_board[21] = 0 # 도착점 점수 0

# 말 4마리의 현재 위치 (모두 시작점 0)
horses = [0, 0, 0, 0]
max_score = 0

def dfs(turn, current_score):
    global max_score
    
    if turn == 10:
        max_score = max(max_score, current_score)
        return

    for i in range(4):
        curr = horses[i]
        
        # 이미 도착한 말은 움직일 수 없음
        if curr == 21:
            continue
            
        # 이동 시작
        # 파란색 칸에서 시작하는지 확인
        if curr in blue:
            nxt = blue[curr]
            step = dice[turn] - 1 # 파란색으로 한칸 갔으니 1 감소
        else:
            nxt = next_node[curr]
            step = dice[turn] - 1 # 일반 이동 한칸 갔으니 1 감소
            
        # 남은 주사위 눈만큼 이동
        while step > 0:
            nxt = next_node[nxt]
            if nxt == 21: # 도착하면 멈춤
                break 
            step -= 1
        
        # 도착 칸이 아닌데, 다른 말이 이미 있다면 이동 불가
        if nxt != 21 and nxt in horses:
            continue
            
        # 백트래킹
        original_pos = horses[i]
        horses[i] = nxt
        
        dfs(turn + 1, current_score + score_board[nxt])
        
        horses[i] = original_pos # 원상복구

dfs(0, 0)
print(max_score)