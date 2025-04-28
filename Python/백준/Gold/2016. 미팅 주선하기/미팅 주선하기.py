from itertools import permutations
import sys
input = sys.stdin.readline

def partner(likes):
    likes = [l[:] for l in likes]
    partners = [[] for _ in range(6)]
    girl_next = [0]*11

    for i in range(6,11):
        partners[likes[i][0]].append(i)

    while True:
        canceled = []

        for i in range(1,6):
            if len(partners[i]) >= 2:
                p = partners[i][0]
                idx = likes[i].index(p)
                for partner in partners[i]:
                    temp_idx = likes[i].index(partner)
                    if temp_idx < idx:
                        canceled.append(p)
                        p = partner
                        idx = temp_idx
                    elif temp_idx > idx:
                        canceled.append(partner)
                partners[i] = [p]

        if not canceled:
            break

        for girl in canceled:
            girl_next[girl] += 1
            next_boy = likes[girl][girl_next[girl]]
            partners[next_boy].append(girl)

    return partners[1]

t = int(input())
for _ in range(t):
    flag = False
    likes = [[], [6,7,8,9,10]]
    for _ in range(9):
        temp = list(map(int, input().split()))
        likes.append(temp)
    init = partner(likes)

    for i in permutations(range(6,11), 5):
        likes[1] = list(i)
        res = partner(likes)
        if res < init:
            flag = True
            break

    print('YES' if flag else 'NO')