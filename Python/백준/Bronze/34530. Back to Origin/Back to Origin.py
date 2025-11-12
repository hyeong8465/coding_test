"""
12:46
1km 이동 후, 시계방향으로 d도만큼 회전, 최소 몇 번의 이동이 필요?

최대 공약수
최소 공배수

"""
d = int(input())


for i in range(360):
    if d*(i+1) % 360 == 0:
        print(i+1)
        quit()
print(-1)

