try:
    while True:
        a, b = map(int,input().split())
        answer = a
        c = a
        while c >= b:
            answer += c//b
            c = c//b + c%b
        print(answer)
except:
    quit()