from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001

queue = deque()
queue.append(N)
visited[N] = 1

while queue:
  x = queue.popleft()

  if x == K:
    print(visited[x] - 1)
    break

  for nx in (x + 1, x - 1, x * 2):
    if 0 <= nx <= 100000 and not visited[nx]:
      visited[nx] = visited[x] + 1
      queue.append(nx)