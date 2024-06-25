from collections import deque

def bfs(x, y, k):
  queue = deque()
  queue.append((x, y, k))
  visited[x][y][k] = 1

  while queue:
    x, y, k = queue.popleft()

    if x == H - 1 and y == W - 1:
      return visited[x][y][k] - 1

    if k < K:
      for i, j in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
        nx = x + i
        ny = y + j

        if 0 <= nx < H and 0 <= ny < W:
          if maps[nx][ny] == 0 and not visited[nx][ny][k + 1]:
            visited[nx][ny][k + 1] = visited[x][y][k] + 1
            queue.append((nx, ny, k + 1))

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if 0 <= nx < H and 0 <= ny < W:
        if maps[nx][ny] == 0 and not visited[nx][ny][k]:
          visited[nx][ny][k] = visited[x][y][k] + 1
          queue.append((nx, ny, k))
  
  return -1

K = int(input())
W, H = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0, 0))

for m in visited:
  print(m)