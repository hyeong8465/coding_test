"""
15:54
1-2-3

"""


def solution(n, lost, reserve):
    reserve_new = list(set(reserve) - set(lost))
    reserve_new.sort()
    lost_new = list(set(lost) - set(reserve))
    lost_new.sort()
    answer = n-len(lost_new)
    print(answer)

    point_lost = 0
    point_reserve = 0
    while point_lost < len(lost_new) and point_reserve < len(reserve_new):
        print(point_lost, point_reserve)
        if abs(lost_new[point_lost] - reserve_new[point_reserve]) == 1:
            answer += 1
            point_lost += 1
            point_reserve += 1
        elif lost_new[point_lost] > reserve_new[point_reserve]:
            point_reserve += 1
        elif lost_new[point_lost] < reserve_new[point_reserve]:
            point_lost += 1
    return answer

