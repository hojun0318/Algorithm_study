from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if not visited[nx][ny]:
          if sea[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            return visited[nx][ny] - 1
          else:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))


N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

ans = 0

dx = [-1, -1, 0, 1, 1,  1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(N):
  for j in range(M):
    visited = [[0] * M for _ in range(N)]
    if sea[i][j] == 0:
      ans = max(ans, bfs(i, j))

print(ans)