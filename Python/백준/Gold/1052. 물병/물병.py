"""
14:18
그리디

모든 물병에는 물이 1리터씩
한 번에 K개의 물병 이동 가능
물 낭비 x, 이동은 한 번만
물병의 물을 적절히 재분배해서 k개를 넘지 않는 비어있지 않은 물병을 만들어라

상점에서 사야하는 물병의 최솟값

n = 3, k = 1
1 1 1
2 1 0
2 1 1 0 <- 하나 구매
2 2 0 0
4 0 0 <-

13: 1 * 13
7: 2 * 6, 1 * 1
4: 4 * 3, 1 * 1
3: 8 * 1, 4 * 1, 1 * 1

100만: 1 * 100만
50만: 2 * 50만
25만: 4*25만
17.5만: 8*17.5만

try1:
몫이 0이 될 때까지 2로 계속 나누면서 나머지가 발생한 부분의 값을 저장
나머지의 갯수가 물병의 개수
k개를 넘으면 필요한만큼의 물병 구매
"""
n, k = map(int, input().split())

i = 0
bottle = []
while True:
    if n == 0:
        # bottle.append(2**i)
        break

    if n % 2 == 0:
        n = n//2
    else:
        n = n//2
        bottle.append(2**i)
    i += 1
# print(bottle)
        
ans = 0

if len(bottle) > k:
    ans = bottle[len(bottle)-k] - sum(bottle[:len(bottle)-k])
print(ans)
    