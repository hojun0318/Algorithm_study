from collections import deque

def bfs(x, y, k, d):
  queue = deque()
  queue.append((x, y, k, d))
  visited[x][y][k] = 1

  while queue:
    x, y, k, d = queue.popleft()

    if x == (N - 1) and y == (M - 1):
      return visited[x][y][k]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if maps[nx][ny] == 1 and k < K:
          if not visited[nx][ny][k + 1]:
            if d % 2 == 0:
              visited[nx][ny][k + 1] = d + 2
              queue.append((nx, ny, k + 1, d + 1))
            else:
              queue.append((x, y, k, d + 1))

        if maps[nx][ny] == 0 and not visited[nx][ny][k]:
          visited[nx][ny][k] = visited[x][y][k] + 1
          queue.append((nx, ny, k, d + 1))

  return - 1

N, M, K = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0, 0, 0))

for m in visited:
  print(m)