from collections import deque

def bfs(x, y, k):
  queue = deque()
  queue.append((x, y, k))
  visited[x][y][k] = 1

  while queue:
    x, y, k = queue.popleft()

    if x == (N - 1) and y == (M - 1):
      return visited[x][y][k]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if k < K:
          if maps[nx][ny] == 1 and not visited[nx][ny][k + 1]:
            visited[nx][ny][k + 1] = visited[x][y][k] + 1
            queue.append((nx, ny, k + 1))
        if maps[nx][ny] == 0 and not visited[nx][ny][k]:
          visited[nx][ny][k] = visited[x][y][k] + 1
          queue.append((nx, ny, k))


  return - 1


N, M, K = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0, 0))