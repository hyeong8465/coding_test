#비밀번호는 6자리 이상 9자리 이하여야 한다.
N = int(input())
for _ in range(N):
    a = input()
    if len(a) >= 6 and len(a) <= 9:
        print("yes")
    else:
        print("no")