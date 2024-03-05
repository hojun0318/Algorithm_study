from collections import deque

N, M = map(int, input().split())
walls = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
  queue = deque()
  queue.append((x, y, h))
  visited[x][y][h] = 1

  while queue:
    x, y, h = queue.popleft()

    if x == (N - 1) and y == (M - 1):
      return visited[x][y][h]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if walls[nx][ny] == 0 and visited[nx][ny][h] == 0:
          visited[nx][ny][h] = visited[x][y][h] + 1
          queue.append((nx, ny, h))
        if walls[nx][ny] == 1 and h == 1 and visited[nx][ny][h - 1] == 0:
          visited[nx][ny][h - 1] = visited[x][y][h] + 1
          queue.append((nx, ny, h - 1))

  return -1

print(bfs(0, 0, 1))