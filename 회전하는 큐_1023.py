from collections import deque

N, M = map(int, input().split())
lst = list(map(int, input().split()))
queue = deque([i for i in range(1, N + 1)])

cnt = 0

for n in lst:
  while True:
    if queue[0] == n:
      queue.popleft()
      break
    else:
      if queue.index(n) < len(queue) / 2:
        while queue[0] != n:
          queue.append(queue.popleft())
          cnt += 1
      else:
        while queue[0] != n:
          queue.appendleft(queue.pop())
          cnt += 1

print(cnt)