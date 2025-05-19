import heapq as hq
import sys
input = sys.stdin.readline
inf = float('inf')

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[inf]*n for _ in range(n)]
    q = [(graph[0][0], 0, 0)]

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while q:
        dis, x, y = hq.heappop(q)
#        print(dis, x, y)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if distance[nx][ny] > dis+graph[nx][ny]:
                    distance[nx][ny] = dis+graph[nx][ny]
                    hq.heappush(q, (dis+graph[nx][ny], nx, ny))

    # for d in distance:
    #     print(d)
    print(f'Problem {cnt}: {distance[-1][-1]}')
    cnt += 1