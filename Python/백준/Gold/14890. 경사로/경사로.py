import sys
input = sys.stdin.readline

def check_line(line):
    # 경사로가 설치된 곳을 체크하기 위한 배열
    used = [False] * n 
    
    for i in range(n - 1):
        # 1. 높이가 같으면 패스
        if line[i] == line[i+1]:
            continue
            
        # 2. 높이 차이가 1보다 크면 불가능
        if abs(line[i] - line[i+1]) > 1:
            return False
            
        # 3. 내리막길 (현재 > 다음): 오른쪽 L개의 칸을 확인
        if line[i] > line[i+1]:
            temp = line[i+1] # 경사로를 놓을 바닥 높이
            for j in range(i+1, i+1+l):
                # 범위 체크, 이미 경사로 놓였는지 체크, 높이 체크
                if 0 <= j < n:
                    if line[j] != temp or used[j]:
                        return False
                    used[j] = True # 경사로 설치
                else:
                    return False
                    
        # 4. 오르막길 (현재 < 다음): 왼쪽 L개의 칸을 확인
        else:
            temp = line[i] # 경사로를 놓을 바닥 높이
            for j in range(i, i-l, -1):
                # 범위 체크, 이미 경사로 놓였는지 체크, 높이 체크
                if 0 <= j < n:
                    if line[j] != temp or used[j]:
                        return False
                    used[j] = True # 경사로 설치
                else:
                    return False
    return True

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 1. 가로 방향 확인
for row in graph:
    if check_line(row):
        ans += 1

# 2. 세로 방향 확인 (지도를 전치행렬로 변환하여 가로처럼 확인)
# zip(*graph)는 행과 열을 바꿔줍니다.
for col in zip(*graph):
    if check_line(col):
        ans += 1

print(ans)