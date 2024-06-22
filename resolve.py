# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(sx, sy):
  queue = deque()
  queue.append((sx, sy))
  visited[sx][sy] = 1

  while queue:
    x, y = queue.popleft()

    if x == ex and y == ey:
      return visited[x][y] - 1

    for i, j in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
      nx = x + i
      ny = y + j

      if 0 <= nx < I and 0 <= ny < I:
        if not visited[nx][ny]:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))


T = int(input())
for _ in range(T):
  I = int(input())
  sx, sy = map(int, input().split())
  ex, ey = map(int, input().split())
  visited = [[0] * I for _ in range(I)]

  print(bfs(sx, sy))