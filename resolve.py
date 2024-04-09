from collections import deque

T = int(input())
for _ in range(T):
  L = int(input())
  maps = [[0] * L for _ in range(L)]
  sx, sy = map(int, input().split())
  ex, ey = map(int, input().split())
  maps[sx][sy] = 1

  queue = deque()
  queue.append((sx, sy))

  while queue:
    x, y = queue.popleft()

    if x == ex and y == ey:
      print(maps[x][y] - 1)
      break

    for dx, dy in ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)):
      nx = x + dx
      ny = y + dy

      if 0 <= nx < L and 0 <= ny < L and not maps[nx][ny]:
        maps[nx][ny] = maps[x][y] + 1
        queue.append((nx, ny))