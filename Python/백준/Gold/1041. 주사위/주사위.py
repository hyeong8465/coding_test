"""
5개의 면에 쓰여 있는 수의 합의 최솟값을 출력
nxnxn크기의 정육면체
꼭지점과 모서리가 중요
꼭짓점 4개 -> 3면 노출: 4개
모서리 그외 모서리 2면 노출: (n-1)*4 + (n-2)*4개
그외 1면 노출 n**3-4-(n-1)*4+(n-2)*4



"""

n = int(input())
a, b, c, d, e, f = map(int, input().split())
case2 = [a+b, a+c,a+d,a+e,b+c,b+d,b+f,c+e,c+f,d+e,d+f,e+f]
case3 = [a+b+c,a+c+e,a+d+e,a+d+b,b+f+d,c+b+f,d+f+e,e+f+c]

# print(min(case2))
# print(min(case3))
if n == 1:
    print(sum([a,b,c,d,e,f])-max([a,b,c,d,e,f]))
    quit()

print(min(case2)*4*(n-1) + min(case2)*4*(n-2) + min(case3)*4 + (n**2*5-4*3-(n-1)*4*2-(n-2)*4*2)*min([a,b,c,d,e,f]))
# print((n**2*5-4*3-(n-1)*4*2-(n-2)*4*2))