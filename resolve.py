from collections import deque

def bfs(x, y, c):
  queue = deque()
  queue.append((x, y, c))
  visited[x][y][c] = 1

  while queue:
    x, y, c = queue.popleft()

    if x == (N - 1) and y == (M - 1):
      return visited[x][y][c]
      
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if maps[nx][ny] == 0 and not visited[nx][ny][c]:
          visited[nx][ny][c] = visited[x][y][c] + 1
          queue.append((nx, ny, c))
        if maps[nx][ny] == 1 and c == 1 and not visited[nx][ny][c - 1]:
          visited[nx][ny][c - 1] = visited[x][y][c] + 1
          queue.append((nx, ny, c - 1))

  
  return -1



N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0, 1))