"""
16:25

1. A-Z의 절반 지점보다 뒤에 있으면 아래 방향키로 이동
2. 좌우 어디로 가야 하는가? 최소 경로를 어떻계? 방문처리를 하지 않는 bfs?
    - JAZ
    - JZAAAZZ
방문처리를 하지 않는 BFS? - x
- 전체 순회를 해서 방문해야 하는 위치("A"가 아닌 곳)을 찾는다.
- BFS로 해당 위치를 모두 방문하는 경로를 찾는다.
- 최대 뎁스가 20 -> 전체 연산량은? 2**20?

방향 전환은 1번이면 충분함
언제 방향 전환을 할 것인가?
    for i in range(len(name)):
        for j in range(i+1, len(name)):
            if name
            


"""

def solution(name):
    answer = 0
    for i, chr in enumerate(name):
        if chr == "A":
            continue
        dis = ord(chr)-65
        answer += min(dis, 26-dis)
    # print(answer)
    dis = float("inf")
    for i in range(len(name)):
        temp = i
        for j in range(i+1, len(name)):
            if name[j] != "A":
                temp = len(name)-j+i*2
                print(i, j, temp)
                break
        dis = min(dis, temp)

    for i in sorted(range(len(name)), reverse = True):
        temp = len(name)-i
        pos = 0
        for j in range(i):
            if name[j] != "A":
                pos = j
        temp = (len(name)-i)*2+pos
        dis = min(dis, temp)
    print(dis, answer)
    return answer+dis

