n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf') # 최소 능력치 차이를 저장할 변수

# 백트래킹 함수 정의
# idx: 현재 처리할 선수의 인덱스 (0부터 n-1까지)
# start_team: 스타트 팀에 포함된 선수들의 인덱스 리스트
def team_selection(idx, start_team):
    global min_diff

    # 1. 종료 조건 (모든 선수를 다 고려했거나, 스타트 팀 인원수가 충분할 때)
    if idx == n:
        # 스타트 팀의 인원이 N/2명이 아니면 유효하지 않은 경우
        if len(start_team) != n // 2:
            return
        
        # 링크 팀 구성
        link_team = []
        all_players = set(range(n)) # 0부터 n-1까지 모든 선수 인덱스
        for i in range(n):
            if i not in start_team:
                link_team.append(i)

        # 능력치 계산
        score_start = 0
        for i in start_team:
            for j in start_team:
                score_start += s[i][j]
        
        score_link = 0
        for i in link_team:
            for j in link_team:
                score_link += s[i][j]
        
        # 최소 능력치 차이 업데이트
        min_diff = min(min_diff, abs(score_start - score_link))
        return

    # 2. 재귀 호출 (현재 선수를 스타트 팀에 포함하는 경우)
    # 스타트 팀의 인원수가 N/2를 초과하지 않도록 가지치기
    if len(start_team) < n // 2:
        start_team.append(idx) # 현재 선수를 스타트 팀에 추가
        team_selection(idx + 1, start_team) # 다음 선수로 재귀 호출
        start_team.pop() # 백트래킹: 추가했던 선수를 다시 제거 (다음 경우를 위해)

    # 3. 재귀 호출 (현재 선수를 스타트 팀에 포함하지 않는 경우 -> 링크 팀으로 간주)
    team_selection(idx + 1, start_team) # 다음 선수로 재귀 호출 (현재 선수는 스타트 팀에 없음)

# 백트래킹 시작 (0번 선수부터 시작, 스타트 팀은 비어있는 상태)
team_selection(0, [])

print(min_diff)