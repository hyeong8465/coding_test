"""
11:30
수빈의 이동: x-1, x+1, 2*x
수빈이가 동생을 찾을 수 있는 가장 빠른 시간?
가장 빠른 시간으로 찾는 방법이 몇 가지?

10만

0 1 2 3 4 5
  x       o
1 -> 2 -> 4 -> 5
1 ->

1 -> 6
1 -> 2 -> 4 -> 5 -> 6
1 -> 2 -> 4 -> 3 -> 6
1 -> 2 -> 3 -> 6

1 -> 10
1 -> 2 -> 4 -> 8 -> 9 -> 10
1 -> 2 -> 4 -> 5 -> 10

모든 점에서 최단 경로의 수 저장?
중간 점까진 최단 경로가 아닌데 최종 점에서 최단 경로일 수 있나? -> 없을 듯
최단 경로가 아니면 continue

"""
from collections import deque
inf = float('inf')

n, m = map(int, input().split())
visited = [[inf, 0] for _ in range(100001)] # [time, cnt]
visited[n] = [0,1]

def bfs(start):
    q = deque([(start, 0)])

    while q:
        x, time = q.popleft()
        if x == m:
            continue
        for i in [x-1, x+1, x*2]:
            if 0<=i<100001:
                if visited[i][0] > time+1:
                    visited[i][0] = time+1
                    visited[i][1] = 1
                    q.append((i, time+1))
                elif visited[i][0] == time+1:
                    visited[i][1] += 1
                    q.append((i, time+1))
                else:
                    continue

bfs(n)
print(visited[m][0])
print(visited[m][1])

                    






