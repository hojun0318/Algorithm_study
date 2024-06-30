from collections import deque

def bfs(x, y):
  now = deque()
  now.append((x, y))

  while now:
    x, y = now.popleft()
    if rooms[x][y]:
      queue = rooms[x][y]

      for _ in range(len(queue)):
        a, b = queue.popleft()
        if visited[a][b] == 0:
          visited[a][b] = 1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if visited[nx][ny] == 1:
          now.append((nx, ny))
          now.append((x, y))



N, M = map(int, input().split())
rooms = [[deque() for _ in range(N + 2)] for _ in range(N + 2)]
visited = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
visited = [[0] * (N + 2)] + [[0] * (N + 2) for _ in range(N)] + [[0] * (N + 2)]
x = y = 1
visited[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(M):
  x, y, a, b = map(int, input().split())
  rooms[x][y].append((a, b))

for m in rooms:
  print(m)

bfs(x, y)


queue = rooms[1][1]