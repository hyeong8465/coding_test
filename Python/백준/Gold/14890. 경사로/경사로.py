"""
14:39
nxn 지도에 각 칸의 높이가 적혀있음
지나갈 수 있는 길의 갯수?
길: 한 행 혹은 한 열 전부, 한쪽 끝에서 다른쪽 끝까지 지나감
지나갈 수 있는:
    1. 길에 속한 모든 칸의 높이가 모두 같아야 함
    2. 경사로를 놓아서 지나갈 수 있어야 함, 경사로의 높이는 항상 1, 길이 
        2-1. L개의 연속된 칸에 경사로의 바닥이 모두 접해야 함
        2-2. 낮은 칸과 높은 칸의 높이 차는 1
        2-3. 낮은 칸의 높이는 모두 같아야하고, L개의 칸이 연속되어 있어야 함.

엣지 케이스
2 - 경사로 - 3 - 경사로 - 2

0. 경사로가 겹치지 않기 위해 경사로 저장할 배열 초기화
1. row 단위로 순회
2-1. 다음 칸이 본인과 같은 숫자면, 
    다음 칸으로 이동
2-2. 다음 칸이 본인보다 낮은 숫자면,
    1. 앞 l개의 칸이 서로 같은 숫자이고 본인과 1차이인지 확인
    2. 조건을 만족하면 경사로 배열에 추가
2-3. 다음 칸이 본인보다 높은 숫자면,
    1. 본인을 포함한 이전 l개의 칸이 서로 같은 숫자이고 다음 칸이 본인과 1차이인지 확인
    2. 조건을 만족하면 경사로 배열에 추가
3. col 단위로 똑같이 확인
"""
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
road = [[0]*n for _ in range(n)]

ans = 0
for row in range(n):
    road_temp = []
    success = True
    for col in range(n-1):
        # print(row, col)
        if graph[row][col] > graph[row][col+1]: # 더 작을 때,
            if col+l >= n: # 범위 초과
                # print(111)
                success = False
                break # 바로 다음 row로 이동

            for c in range(col+1, col+1+l):
                if road[row][c] != 0 or graph[row][c] != graph[row][col]-1:
                    # print(222)
                    success = False
                    break
                else:
                    road_temp.append((row, c))
        
        elif graph[row][col] < graph[row][col+1]: # 더 클 때,
            if col-l+1 < 0:
                # print(333)
                success = False
                break # 바로 다음 row로 이동

            for c in range(col+1-l, col+1):
                # print("c", c)
                if road[row][c] != 0 or graph[row][c] != graph[row][col+1]-1:
                    # print(444)
                    success = False
                    break
                else:
                    road_temp.append((row, c))    
        if len(set(road_temp)) != len(road_temp):
            success = False
        if not success:
            break
    if success:
        ans += 1
        for x,y in road_temp:
            road[x][y] = 1
        # print("row", row, "ans", ans)
road = [[0]*n for _ in range(n)]
for col in range(n):
    road_temp = []
    success = True
    for row in range(n-1):
        # print(row, col)
        if graph[row][col] > graph[row+1][col]: # 더 작을 때,
            if row+l >= n: # 범위 초과
                # print(111)
                success = False
                break # 바로 다음 row로 이동

            for r in range(row+1, row+1+l):
                if road[r][col] != 0 or graph[r][col] != graph[row][col]-1:
                    # print(222)
                    success = False
                    break
                else:
                    road_temp.append((r, col))
        
        elif graph[row][col] < graph[row+1][col]: # 더 클 때,
            if row-l+1 < 0:
                # print(333)
                success = False
                break # 바로 다음 row로 이동

            for r in range(row+1-l, row+1):
                # print("c", c)
                if road[r][col] != 0 or graph[r][col] != graph[row+1][col]-1:
                    # print(444)
                    success = False
                    break
                else:
                    road_temp.append((r, col))    
        if len(set(road_temp)) != len(road_temp):
            success = False
        if not success:
            break
    if success:
        ans += 1
        for x,y in road_temp:
            road[x][y] = 1
        # print("col", col, "ans", ans)
print(ans)