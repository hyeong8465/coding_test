"""
10:47

최대 2명이 탑승 가능한 구명보트 + 무게 제한
구명보트 최대한 적게 사용

최대한 무게제한에 맞추면 되는데
정렬 - 좌우 끝에서 하나씩?
투포인터


"""
def solution(people, limit):
    answer = 0
    l, r = 0, len(people)-1
    people.sort()

    while l<r:
        if people[l]+people[r] <= limit:
            answer += 1
            l += 1
            r -= 1
        else:
            r -= 1

    answer += len(people)-2*answer # 남은 인원
    print(answer)

    return answer