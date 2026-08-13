def solution(progresses, speeds):
    days = [-(-(100 - p) // s) for p, s in zip(progresses, speeds)]  # ceil division

    answer = []
    count = 0
    max_day = days[0]
    for d in days:
        if d <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = d
            count = 1
    answer.append(count)

    return answer