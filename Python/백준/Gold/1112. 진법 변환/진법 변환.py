"""
b: 절대값이 2~10사이
"""

x, b = input().split()

def sol(x, b):
    answer = ''
    x = abs(int(x))
    b = int(b)

    while x > 0:
        x, mod = divmod(x,b)
        answer += str(mod)
    
    return answer[::-1]

def sol2(x,b):
    answer = ''
    x = int(x)
    b = int(b)

    while x != 0:
        i, mod = divmod(x,b)
        # print(i,mod)
        if i*b > x:
            nx = i+1
            mod = x - b*nx
        else:
            nx = i
            mod = mod
        # mod = x%i
        x = nx
        # print(x, mod)
        # if mod != 0:
        #     mod = x%(i+1)
        #     x = i+1
        # else:
        #     x = i
        answer+=str(mod)
        # print(answer, 111111)
    return answer[::-1]

if int(x) == 0:
    print(0)

if b[0] == '-':
    print(sol2(x,b))
else:
    if x[0] == '-':
        print('-'+sol(x,b))
    else:
        print(sol(x,b))

