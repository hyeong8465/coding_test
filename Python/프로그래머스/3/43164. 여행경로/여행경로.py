from collections import defaultdict
def dfs2(tickets_dict, dep, n, route):
    global answer2
    if len(route) == n + 1:
        if not answer2 or route < answer2:
            answer2 = route[:]
        return

    for arr in sorted(set(tickets_dict[dep])):
        tickets_dict[dep].remove(arr)
        route.append(arr)
        dfs2(tickets_dict, arr, n, route)
        route.pop()
        tickets_dict[dep].append(arr)


def solution(tickets):
    n = len(tickets)
    tickets_dict = defaultdict(list)
    for dep, arr in tickets:
        tickets_dict[dep].append(arr)
    global answer2
    answer2 = []
    dfs2(tickets_dict, "ICN", n, ["ICN"])
    return answer2

# print(solution2(tickets))
