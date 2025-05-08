
n = int(input())
arr = []
for _ in range(n):
	a, b = map(int, input().split())
	arr.append((a,'s'))
	arr.append((b,'e'))

arr.sort(key = lambda x:(x[0], x[1]))

room = 0 # 회의실
res = 0 # 필요한 최소 회의실
q = [0] # 가장 빨리 끝나는 회의실 저장

# heapq.heappush()
for time, state in arr:
	if state == 's':
		# heapq.heappush(q[0])
		room += 1
		res = max(res, room)
	else:
		room-=1
print(res)