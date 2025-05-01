import sys
input = sys.stdin.readline

n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

result = {-1:0, 0:0, 1:0}

def check(papers):
    plag = False
    temp = papers[0][0]
    for paper in papers:
        for p in paper:
            if p != temp:
                plag = True
                break
    if plag:
        a = len(papers)//3
        for i in range(3):
            for j in range(3):
                sub = [row[j*a:(j+1)*a] for row in papers[i*a:(i+1)*a]]
                check(sub)
    else:
        result[temp] += 1

check(papers)
for k, v in result.items():
    print(v)
    
    
    
