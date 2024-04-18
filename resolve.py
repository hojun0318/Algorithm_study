from collections import deque

def bfs(x, y, h):
  queue = deque()
  queue.append((x, y, h))

  while queue:
    x, y, h = queue.popleft()

    if x == (H - 1) and y == (W - 1):
      return visited[x][y][h]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][h] and maps[nx][ny] == 0:
        queue.append((nx, ny, h))
        visited[nx][ny][h] = visited[x][y][h] + 1
    
    if h < K:
      for j in range(8):
        nx = x + hx[j]
        ny = y + hy[j]

        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][h + 1] and maps[nx][ny] == 0:
          queue.append((nx, ny, h + 1))
          visited[nx][ny][h + 1] = visited[x][y][h] + 1

  return - 1



K = int(input())
W, H = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

hx = [-1, -2, -2, -1, 1, 2, 2, 1]
hy = [2, 1, -1, -2, -2, -1, 1, 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0, 0))