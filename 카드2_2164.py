from collections import deque

N = int(input())
queue = deque()

for i in range(1, N + 1):
  queue.append(i)

while True:
  if len(queue) == 1:
    break
  else:
    queue.popleft()

  queue.append(queue.popleft())

print(queue[0])