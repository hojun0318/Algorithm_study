from collections import deque

def bridge(x, y, c):
  queue = deque()
  queue.append((x, y, c))

  while queue:
    x, y, c = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if maps[nx][ny] == 0 and not bridge_visited[nx][ny]:
          bridge_visited[nx][ny] = bridge_visited[x][y] + 1
          queue.append((nx, ny, c))
        elif maps[nx][ny] != c and maps[nx][ny] != 0:
          return bridge_visited[x][y]

  return N

def bfs(x, y):
  global cnt
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if maps[nx][ny] == 1 and not visited[nx][ny]:
          visited[nx][ny] = 1
          maps[nx][ny] = cnt
          queue.append((nx, ny))


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
ans = 9999999

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(N):
  for j in range(N):
    if maps[i][j] == 1 and not visited[i][j]:
      cnt += 1
      visited[i][j] = 1
      maps[i][j] = cnt
      bfs(i, j)

for r in range(N):
  for c in range(N):
    bridge_visited = [[0] * N for _ in range(N)]
    if maps[r][c] != 0:
      cursor = maps[r][c]
      ans = min(ans, bridge(r, c, cursor))

print(ans)