import sys
input = sys.stdin.readline

n = int(input())
hand = list(map(int, input().split()))
hand_dic = {}
for i in hand:
    if i in hand_dic:
        hand_dic[i] += 1
    else:
        hand_dic[i] = 1
input()
card = list(map(int, input().split()))
for i in card:
    try: 
        print(hand_dic[i], end=' ')
    except:
        print(0, end = ' ')