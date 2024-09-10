
N, score, P = map(int,input().split())
if N == 0:
    print(1)
    quit()
ranking = list(map(int,input().split()))
if N < P:
    if score in ranking:
            idx_f = ranking.index(score)
            print(idx_f+1)
        # 점수 유일
    else:
        ranking.append(score)
        ranking.sort(reverse=True)
        idx = ranking.index(score)
        print(idx+1)
else:
    # 순위에 못 드는 경우
    if score == ranking[-1] or score < ranking[-1]:
         print(-1)
    # 순위에 드는 경우
    else:
        # 점수 중복
        if score in ranking:
            idx_f = ranking.index(score)
            print(idx_f+1)
        # 점수 유일
        else:
            ranking.append(score)
            ranking.sort(reverse=True)
            idx = ranking.index(score)
            print(idx+1)