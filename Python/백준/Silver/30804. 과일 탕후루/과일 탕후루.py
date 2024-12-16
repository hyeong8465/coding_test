n = int(input())
stick = list(map(int, input().split()))

ans = 0
left = 0
fruit = {}
num_fruit = 0

for right in range(n):
    if stick[right] in fruit:
        fruit[stick[right]] += 1
    else:
        fruit[stick[right]] = 1
        num_fruit += 1

    while num_fruit > 2:
        fruit[stick[left]] -= 1
        if fruit[stick[left]] == 0:
            num_fruit -= 1
            del fruit[stick[left]]
        left += 1
    ans = max(ans, right - left + 1)

print(ans)