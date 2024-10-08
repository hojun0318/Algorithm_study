from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  maps[x][y] = 0

  while queue:
    x, y = queue.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < h and 0 <= ny < w:
        if maps[nx][ny] == 1:
          maps[nx][ny] = 0
          queue.append((nx, ny))

  return


while True:
  w, h = map(int, input().split())

  if w == h == 0:
    break

  maps = [list(map(int, input().split())) for _ in range(h)]

  dx = [-1, -1, 0, 1, 1,  1,  0, -1] 
  dy = [ 0,  1, 1, 1, 0, -1, -1, -1]
  ans = 0

  for i in range(h):
    for j in range(w):
      if maps[i][j] == 1:
        ans += 1
        bfs(i, j)

  print(ans)