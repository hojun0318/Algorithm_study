from collections import deque

N, M, K = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, k):
  queue = deque()
  queue.append((x, y, k))

  while queue:
    x, y, k = queue.popleft()

    if x == (N - 1) and y == (M - 1):
      return visited[x][y][k]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if visited[nx][ny][k] == 0 and matrix[nx][ny] == 0:
          queue.append((nx, ny, k))
          visited[nx][ny][k] = visited[x][y][k] + 1

        if k < K:
          if matrix[nx][ny] == 1 and visited[nx][ny][k + 1] == 0:
            queue.append((nx, ny, k + 1))
            visited[nx][ny][k + 1] = visited[x][y][k] + 1
  
  return -1


print(bfs(0, 0, 0))