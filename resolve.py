# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs():
  queue = deque()

  for l in range(L):
    for r in range(R):
      for c in range(C):
        if buildings[l][r][c] == 'S':
          visited[l][r][c] = 1
          queue.append((l, r, c))

  while queue:
    z, x, y = queue.popleft()

    if buildings[z][x][y] == 'E':
      return f'Escaped in {visited[z][x][y] - 1} minute(s).'

    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
        if not visited[nz][nx][ny] and buildings[nz][nx][ny] != '#':
          visited[nz][nx][ny] = visited[z][x][y] + 1
          queue.append((nz, nx, ny))

  return "Trapped!"

while True:
  L, R, C = map(int, input().split())
  if L == 0 and R == 0 and C == 0:
    break

  visited = [[[0] * C for _ in range(R)] for _ in range(L)]  
  buildings = []

  for _ in range(L):
    buildings.append([list(map(str, input())) for _ in range(R)])
    temp = input()

  dz = [1, -1, 0, 0, 0, 0]
  dx = [0, 0, -1, 1, 0, 0]
  dy = [0, 0, 0, 0, -1, 1]

  print(bfs())