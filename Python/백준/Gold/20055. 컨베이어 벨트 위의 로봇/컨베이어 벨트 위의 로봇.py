"""
10:24
길이가 2N인 벨트
시계방향으로 회전
1번 칸: 올리는 위치, N번 칸: 내리는 위치
로봇을 올리거나 옮기면 내구도 1감소

1. 벨트 1칸 회전 -> deque pop, append left
2. 로봇이 벨트가 회전하는 방향으로 한 칸 이동, 이동할 수 없다면 가만히 서 있음 -> 로봇울 저장할 deque
    2-1. 이동하기 위해서는 이동하려는 칸에 로봇이 없고 그 칸의 내구도가 1이상 있어야 함
    이동하려는 칸에 로봇이
4. 올리는 위치에 있는 칸의 내구도가 0이 아니라면 올리는 위치에 로봇을 올림
5. 내구도가 0인 칸의 개수가 k개 이상아면 종료

종료되었을 때 몇 번째 단계가 진행 중이었는지 출력

시뮬

"""
from collections import deque

n, k = map(int, input().split())
naegus = deque(list(map(int, input().split())))
robots = deque([0]*n)
# print(naegus)

ans = 0
while True:
# for _ in range(3):
    ans += 1
    # 회전
    last = naegus.pop()
    naegus.appendleft(last)
    # print("내구도 회전:", naegus)
    
    last = robots.pop()
    robots.appendleft(0)
    if robots[-1] != 0:
        robots[-1] = 0
    # print("로봇 회전:",robots)

    # 이동
    for i in range(n-2,-1,-1):
        if robots[i] == 0: continue
        if robots[i+1] == 0 and naegus[i+1] >= 1:
            robots[i+1] = robots[i]
            robots[i] = 0
            naegus[i+1] -= 1
    if robots[-1] != 0:
        robots[-1] = 0
    
    # print("이동 후 내구도:", naegus)
    # print("이동 후 로봇:", robots)

    # 새로운 로봇    
    if naegus[0] != 0:
        robots[0] = 1
        naegus[0] -= 1
        # print("새로운 로봇 추가:", robots)
        # print("새로운 로봇 추가 후 내구도:", naegus)

    cnt = naegus.count(0) # -> 최적화할 수 있는 포인트
    if cnt >= k:
        print(ans)
        break
    # print("==="*10)
        
"""
문제를 잘 읽자
로봇은 N*2번째 칸에서 내리는게 아니라 n번째 칸에서 내림


"""



