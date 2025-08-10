from collections import deque

s = list(input())
t = list(input())

s_que = deque(s)
t_que = deque(t)

reverse = 0
while len(t_que) > len(s_que):
    if reverse: # 역방향
        back = t_que.popleft() # 앞에서 뺌
    else: # 순방향
        back = t_que.pop() # 뒤에서 뺌
    # print(back)
    
    if back =='A':
        continue
    else:
        reverse = (reverse + 1) % 2
    # print(t_que)
    
if reverse:
    t = list(t_que)[::-1]
else:
    t = list(t_que)

# print(t, s)
if t == s:
    print(1)
else:
    print(0)