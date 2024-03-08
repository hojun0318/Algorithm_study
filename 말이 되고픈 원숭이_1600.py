from collections import deque

K = int(input())
W, H = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(H)]

visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

ans = 0

flag = True

hx = [-1, -2, -2, -1, 1, 2, 2, 1]
hy = [2, 1, -1, -2, -2, -1, 1, 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, k):
  queue = deque()
  queue.append((x, y, k))

  while queue:
    x, y, k = queue.popleft()
    if x == (H - 1) and y == (W - 1):
      return visited[x][y][k]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k] and maps[nx][ny] == 0:
        queue.append((nx, ny, k))
        visited[nx][ny][k] = visited[x][y][k] + 1
      
    if k < K:
      for j in range(8):
        nx = x + hx[j]
        ny = y + hy[j]

        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k + 1] and maps[nx][ny] == 0:
          queue.append((nx, ny, k + 1))
          visited[nx][ny][k + 1] = visited[x][y][k] + 1

  return -1

print(bfs(0, 0, 0))

for i in visited:
  print(i)