from sys import stdin
input = stdin.readline

n = int(input())
flowers = []

for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    # 3월 1일 이전에 끝나는 꽃은 무시, 12월 이후 시작도 무시
    if (em < 3 or (em == 3 and ed < 1)) or (sm > 11):
        continue
    flowers.append((sm * 100 + sd, em * 100 + ed))  # 날짜를 MMDD로 정수화

flowers.sort()  # 시작 날짜 기준 정렬

cur = 301  # 3월 1일
end = 0
idx = 0
answer = 0

while cur < 1201:
    max_end = 0
    while idx < len(flowers) and flowers[idx][0] <= cur:
        max_end = max(max_end, flowers[idx][1])
        idx += 1
    if max_end == 0:
        print(0)
        exit()
    cur = max_end
    answer += 1

print(answer)