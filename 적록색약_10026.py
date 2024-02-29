from collections import deque
N = int(input())

graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1
  current_color = graph[x][y]
  if current_color == 'G':
    graph[x][y] = 'R'
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == current_color and visited[nx][ny] == 0:
        queue.append((nx, ny))
        visited[nx][ny] = 1
        if graph[nx][ny] == 'G':
          graph[nx][ny] = 'R'

  return 1

for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      cnt += bfs(i, j)

visited = [[False] * N for _ in range(N)]

for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      ans += bfs(i, j)

print(cnt, ans)