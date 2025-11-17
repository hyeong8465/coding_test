"""
12:03
그리디

물웅덩이 1~10,000개
널빤지 길이: 1~1,000,000

0~10억



"""
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
woongs = [list(map(int, input().split())) for _ in range(n)]
woongs.sort(key=lambda x:x[0])

idx = 0
answer = 0
for s,e in woongs:
    if idx < s:
        cover_start = s
    else:
        cover_start = idx
    
    if cover_start >= e:
        continue
    
    length_to_cover = e-cover_start
    temp = (length_to_cover+l-1)//l
    answer += temp
    idx = cover_start+temp*l
        
print(answer)