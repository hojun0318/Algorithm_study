from collections import deque

N, K = map(int, input().split())

queue = deque()

for i in range(1, N + 1):
  queue.append(i)

ans = []

while queue:
  for _ in range(K - 1):
    queue.append(queue.popleft())
  ans.append(str(queue.popleft()))

print("<",", ".join(ans)[:],">", sep='')