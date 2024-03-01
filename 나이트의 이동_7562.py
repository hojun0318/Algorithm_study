from collections import deque

T = int(input())

for test_case in range(T):
  I = int(input())
  matrix = [[0] * I for _ in range(I)]
  sx, sy = map(int, input().split())
  ex, ey = map(int, input().split())
  queue = deque()
  queue.append((sx, sy))

  dx = [-1, -2, -2, -1, 1, 2, 2, 1]
  dy = [2, 1, -1, -2, -2, -1, 1, 2]

  while queue:
    x, y = queue.popleft()
    if x == ex and y == ey:
      break

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < I and 0 <= ny < I and matrix[nx][ny] == 0:
        matrix[nx][ny] = matrix[x][y] + 1
        queue.append((nx, ny))

  print(matrix[ex][ey])