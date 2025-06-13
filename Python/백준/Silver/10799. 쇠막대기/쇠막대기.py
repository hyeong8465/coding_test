"""
10:53

인접한 ()쌍은 레이저
아닌 (, )는 쇠막대기

길이 10만

스택
열자마자 닫히는 경우 추적할 변수 1개
전체를 저장할 스택 하나
결과값 저장할 변수 하나
"""
text = input()

state = False
stack = []
ans = 0
for t in text:
    if t == '(': # 열림은 그냥 저장
        stack.append(t)
        state = True
    else: # 닫힘
        stack.pop()
        if state:
            ans += len(stack)
        else:
            ans += 1
        state = False
print(ans)
