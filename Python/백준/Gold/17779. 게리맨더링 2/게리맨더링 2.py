import sys
input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

ans = float("inf")

# 1. 모든 가능한 x, y, d1, d2 순회
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):            
            for d2 in range(1, n):
                # 문제의 경계 조건 체크
                if x + d1 + d2 >= n: continue
                if y - d1 < 0 or y + d2 >= n: continue

                # 2. 경계선 그리기 및 선거구 할당을 위한 임시 배열
                temp = [[0] * n for _ in range(n)]
                
                # 5번 선거구 경계선 표시
                for i in range(d1 + 1):
                    temp[x + i][y - i] = 5
                    temp[x + d2 + i][y + d2 - i] = 5
                for i in range(d2 + 1):
                    temp[x + i][y + i] = 5
                    temp[x + d1 + i][y - d1 + i] = 5

                # 3. 5번 선거구 내부 채우기
                # 각 행을 훑으면서 5번 경계 사이를 5로 채움
                for r in range(x + 1, x + d1 + d2):
                    # 해당 행에서 5번이 처음 등장하는 곳부터 마지막 등장하는 곳까지 채우기
                    start = -1
                    end = -1
                    
                    for c in range(n):
                        if temp[r][c] == 5:
                            if start == -1: start = c
                            else: end = c
                    
                    if start != -1 and end != -1:
                        for c in range(start + 1, end):
                            temp[r][c] = 5

                # 4. 인구수 집계
                # count 배열: [dummy, 1번, 2번, 3번, 4번, 5번]
                count = [0] * 6
                
                for r in range(n):
                    for c in range(n):
                        if temp[r][c] == 5:
                            count[5] += people[r][c]
                            temp[r][c] = 5
            
                # 1번 구역 채우기
                for r in range(x + d1):
                    for c in range(y + 1):
                        if temp[r][c] == 5: break # 경계선 만나면 중단
                        count[1] += people[r][c]
                        temp[r][c] = 1

                # 2번 구역 채우기
                for r in range(x + d2 + 1):
                    for c in range(n - 1, y, -1): # 오른쪽 끝에서부터 안쪽으로
                        if temp[r][c] == 5: break
                        count[2] += people[r][c]
                        temp[r][c] = 2

                # 3번 구역 채우기
                for r in range(x + d1, n):
                    for c in range(y - d1 + d2):
                        if temp[r][c] == 5: break
                        count[3] += people[r][c]
                        temp[r][c] = 3

                # 4번 구역 채우기
                for r in range(x + d2 + 1, n):
                    for c in range(n - 1, y - d1 + d2 - 1, -1): # 오른쪽 끝에서부터
                        if temp[r][c] == 5: break
                        count[4] += people[r][c]
                        temp[r][c] = 4
                
                # 5. 최대-최소 갱신
                # count[1:] -> 0번 인덱스 제외한 나머지 구역 인구수 리스트
                curr_max = max(count[1:])
                curr_min = min(count[1:])
                
                ans = min(ans, curr_max - curr_min)
                # if (x,y,d1,d2) == (0,1,1,7):
                #     for t in temp:
                #         print(t)
print(ans)