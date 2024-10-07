import sys
input = sys.stdin.readline

formula = input().rstrip().split('-')
# print(formula)
answer = sum(list(map(int, formula[0].split('+'))))
for i in formula[1:]:
    answer -= sum(list(map(int, i.split('+'))))
print(answer)