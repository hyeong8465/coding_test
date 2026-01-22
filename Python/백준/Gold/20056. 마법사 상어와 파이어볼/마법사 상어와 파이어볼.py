"""
14:00

파이어볼: 위치, 질량, 방향, 속력
1-based index, N-1연결

1. 방향으로 속력만큼 이동, 이동 중엔 같은 칸에 여러 개의 파이어볼이 있을 수 있음
2. 이동이 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서
    1. 파이어볼은 모두 하나로 합쳐짐
    2. 4개로 나누어짐
    3. 나누어진 파이어볼의 질량, 속력, 방향
        질량: 질량합//5
        속력: 속력합//갯수
        방향: 모두 홀수 혹은 짝수이면, 방향은 0,2,4,6 - 그렇지 않으면 1, 3, 5, 7
    4. 질량이 0인 파이어볼은 소멸

k번 이동한 후, 남아있는 파이어볼의 질량의 합?

시뮬

시간복잡도: O(K*N**2) = 2,500,000 2백5십만

move: fireballs 이동, 방문처리를 하며 같은 칸의 좌표를 리스트로 리턴

merge_and_split: 좌표를 기반으로 처리

"""
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [[None]*n for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1] = [(m, s, d)]
# for b in board:
#     print(b)
    
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def move(board):
    
    nboard = [[None]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not board[i][j]: continue
            
            for m, s, d in board[i][j]:
                ni, nj = (i+dx[d]*s)%n, (j+dy[d]*s)%n
                # print(ni, nj)
                if nboard[ni][nj]: # 이미 존재하는 파이어볼이 있으면
                    nboard[ni][nj].append((m,s,d))
                else: # 
                    nboard[ni][nj] = [(m,s,d)]
    
    return nboard

def merge_and_split(board):
    for i in range(n):
        for j in range(n):
            if not board[i][j]: continue

            if len(board[i][j]) >= 2:
                new_fireballs = []
                nm = 0
                ns = 0
                nd = None
                mod_for_nd = 0
                for m, s, d in board[i][j]:
                    nm += m
                    ns += s
                    mod_for_nd += d%2
                    # if i == 4 and j == 2:
                    #     print(d)
                    #     print(mod_for_nd)
                nm = nm//5
                ns = ns//len(board[i][j])
                if nm == 0:
                    board[i][j] = []
                    continue
                # if i == 4 and j == 2:
                #     print(board[i][j])
                #     print(mod_for_nd)
                if mod_for_nd == len(board[i][j]) or mod_for_nd == 0:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]
                
                for d in nd:
                    new_fireballs.append((nm, ns, d))
                
                board[i][j] = new_fireballs
                    
for _ in range(k):
    board = move(board)
    
    # for b in board:
    #     print(b)
    # print("===이동 완료===")
    
    merge_and_split(board)
    # for b in board:
    #     print(b)
    # print("===머지스플릿 완료===")

ans = 0
for i in range(n):
    for j in range(n):
        if not board[i][j]: continue
        for m,s,d in board[i][j]:
            ans += m
print(ans)
            




                    









        
