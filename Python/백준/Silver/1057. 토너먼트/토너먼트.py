# 입력
n, a, b = map(int, input().split())

# 라운드 초기화
round = 0

# a와 b의 번호가 같아질 때까지 반복
while a != b:
    # 한 라운드 진행
    round += 1
    
    # a의 다음 라운드 번호 계산
    a = (a + 1) // 2
    
    # b의 다음 라운드 번호 계산
    b = (b + 1) // 2

# 최종 라운드 출력
print(round)