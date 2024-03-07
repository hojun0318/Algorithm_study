from collections import deque

MAX = 100001
visited = [0] * (MAX)
N, K = map(int, input().split())


def bfs(x, y):
  queue = deque()

  if x == 0:
    queue.append(1)
  else:
    queue.append(x)

  while queue:
    x = queue.popleft()

    if y == x:
      return visited[x]
    
    for nx in (x - 1, x + 1, x * 2):
      if 0 <= nx < MAX and visited[nx] == 0:
        if nx == x * 2:
          visited[nx] = visited[x]
          queue.appendleft(nx)
        else:
          visited[nx] = visited[x] + 1
          queue.append(nx)

if N == 0:
  print(bfs(N, K) + 1)

else:
  print(bfs(N, K))