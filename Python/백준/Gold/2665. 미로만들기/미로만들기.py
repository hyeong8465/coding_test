# try 2
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
miro = [list(map(int, list(input().rstrip()))) for _ in range(n)]

inf = float('inf')
distance = [[inf]*n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = [(0,0,0)]

def dijkstra():
    while q:
        dis, x, y = hq.heappop(q)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                d = distance[nx][ny]
                if miro[nx][ny] == 0: # 벽
                    if dis+1 < d:
                        distance[nx][ny] = dis+1
                        hq.heappush(q, (dis+1, nx, ny))
                else: # 통로
                    if dis < d:
                        distance[nx][ny] = dis
                        hq.heappush(q, (dis, nx, ny))
    return distance[-1][-1]

print(dijkstra())