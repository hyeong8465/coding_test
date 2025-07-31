import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
cargos = list(map(int, input().split()))

cranes.sort(reverse=True)
cargos.sort(reverse=True)

if cranes[0] < cargos[0]:
    print(-1)
else:
    time = 0
    while cargos:
        time += 1
        for crane in cranes:
            if cargos and crane < cargos[-1]:
                break
            for cargo in cargos:
                if crane >= cargo:
                    cargos.remove(cargo)
                    break
                
    print(time)