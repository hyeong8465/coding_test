"""
10:17
장르 별로 가장 많이 재생된 노래 2개
장르 -> 장르 내 노래 -> 재생 횟수가 tie 조건일 땐 고유번호가 낮은 것 우선

정렬




"""
def solution(genres, plays):
    answer = []
    # genres_plays = []
    genres_dict = {} # genre:[total_plays, [(고유번호, plays), (), ...]]
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in genres_dict:
            genres_dict[g][0] += p
            genres_dict[g][1].append((i, p))
            
        else:
            genres_dict[g] = [p, [(i, p)]]
            
    l = []
    for k, v in genres_dict.items():
        l.append((k,v[0]))
    l.sort(key = lambda x: -x[1])
    
    for genre, _ in l:
        genres_dict[genre][1].sort(key = lambda x : (-x[1], x[0]))
        for val in genres_dict[genre][1][:min(2, len(genres_dict[genre][1]))]:
            answer.append(val[0])
    
    return answer