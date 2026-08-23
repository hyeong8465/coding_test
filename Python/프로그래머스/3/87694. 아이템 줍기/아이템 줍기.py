"""
18:18

사각형은 최대 4개
1. 큐에 넣기 전 사각형 안에 있는 좌표인지 확인 -> 별도의 함수로 모듈화 -> O(4)
2. 격자점에 사각형 그리기 -> O()
3. bfs

"""
from collections import deque

# 1. 체크 함수
def checked(rectangle, x, y, nx, ny):
    mx2, my2 = x+nx, y+ny
    # print("check:", x,y)
    inside_any = False
    for lr_x, lr_y, ru_x, ru_y in rectangle:
        if 2*lr_x < mx2 < 2*ru_x and 2*lr_y < my2 < 2*ru_y:
            return False
        if 2*lr_x <= mx2 <= 2*ru_x and 2*lr_y <= my2 <= 2*ru_y:
            inside_any = True

    return inside_any

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 2. graph 그리기
    graph = [[0]*52 for _ in range(52)]
    for lr_x, lr_y, ru_x, ru_y in rectangle:
        for y in range(lr_y, ru_y+1):
            for x in range(lr_x, ru_x+1):
                graph[y][x] = 1
    # for g in graph:
    #     print(*g)
    # 인접하지만 연결되어 있지 않은 경우가 표현이 안됨
    # 음,,
    # 3. bfs
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[False]*52 for _ in range(52)]
    q = deque([(characterX, characterY, 0)])
    visited[characterY][characterX] = True

    while q:
        x, y, cnt = q.popleft()
        # print(x, y, cnt)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if graph[ny][nx] == 1 and not visited[ny][nx] and checked(rectangle, x, y, nx, ny):
                if nx == itemX and ny == itemY:
                    return cnt+1
                q.append((nx,ny,cnt+1))
                visited[ny][nx] = True