from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

group = [[-1]*m for _ in range(n)]
group_dic = {}
group_id = 0

def bfs(x, y, group_id):
    q = deque([(x, y)])
    group[x][y] = group_id
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and group[nx][ny] == -1:
                    group[nx][ny] = group_id
                    cnt += 1
                    q.append((nx, ny))
    group_dic[group_id] = cnt

# 그룹 나누기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and group[i][j] == -1:
            bfs(i, j, group_id)
            group_id += 1

# 출력
for i in range(n):
    row = []
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 1
            neighbor_groups = set()
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m:
                    gid = group[ni][nj]
                    if gid != -1:
                        neighbor_groups.add(gid)
            for gid in neighbor_groups:
                cnt += group_dic[gid]
            row.append(str(cnt % 10))
        else:
            row.append('0')
    print(''.join(row))