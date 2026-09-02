"""
10:47 -> 11:03

최대 2명이 탑승 가능한 구명보트 + 무게 제한
구명보트 최대한 적게 사용

최대한 무게제한에 맞추면 되는데
정렬 - 좌우 끝에서 하나씩?
투포인터

시간 복잡도 O(NlogN + N) = O(NlogN)

"""
def solution(people, limit):
    answer = 0
    l, r = 0, len(people)-1
    people.sort()

    while l<=r:
        if people[l]+people[r] <= limit:
            l += 1
        answer += 1
        r -= 1

    # print(answer)

    return answer