n, w, L = map(int, input().split())
queue = list(map(int, input().split()))

bridge = [0] * w
time = 0

while bridge:
	time += 1
	bridge.pop(0)
	if queue:
		if sum(bridge) + queue[0] <= L:
			bridge.append(queue.pop(0))
		else:
			bridge.append(0)

print(time)