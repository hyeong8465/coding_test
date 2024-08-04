'''
폭발 시 인접한 폭탄은 파괴됨
폭탄은 3초가 지난 후 폭발
1. 0초: 일부 칸에 폭탄 설치
2. 1초: 아무것도 안함
3. 2초: 폭탄이 설치되지 않은 칸에 폭탄 설치 4,6,8,10, ...
4. 3초: 0초에 설치한 폭탄 폭발 5, 7, 9, ...
3,4 반복

4초: 폭탄 설치
5초: 2초에 설치한 폭탄 폭발
6초: 폭탄 설치
7초: 

계속 터지고 설치하고 반복, 공백 없음

.빈칸 O폭탄
'''
# R C N 입력 row col 초
R, C, N = map(int,input().split())
rows = []

for _ in range(R):
    rows.append(input())
# N = 3
# rows = ['.......', '...O...','....O..','.......','OO.....','OO.....']
for sec in range(1, N+1):
    if sec >=2 and sec%2 ==0:
        idx = []
        # 기존 폭탄의 인덱스 저장
        for i, row in enumerate(rows):
            for col in range(C):
                if row[col] == 'O':
                    idx.append([i,col])
                    # print(idx)
        # 폭탄 설치
        for i, row in enumerate(rows):
            rows[i] = row.replace('.', 'O')
    if sec >=2 and sec%2 == 1:
        for i in idx:
            r, c = i[0], i[1]
            # print(rows[r])
            rows[r] = rows[r][:c]+'.'+rows[r][c+1:]
            if r != R-1:
                rows[r+1] = rows[r+1][:c]+'.'+rows[r+1][c+1:]
            if r != 0:
                rows[r-1] = rows[r-1][:c]+'.'+rows[r-1][c+1:]
            if c != 0:
                rows[r] = rows[r][:c-1]+'.'+rows[r][c:]
            if c != C-1:
                rows[r] = rows[r][:c+1]+'.'+rows[r][c+2:]
            # print(rows[r], r, c)
    # print(sec, rows)


for row in rows:
    print(row)          