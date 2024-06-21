# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs():
  ans = 0
  queue = deque()
  
  for k in range(H):
    for i in range(N):
      for j in range(M):
        if boxs[k][i][j] == 1:
          queue.append((k, i, j))
          
  while queue:
    z, x, y = queue.popleft()

    for v in range(2):
      nz = z + dz[v]

      if 0 <= nz < H:
        if boxs[nz][x][y] == 0:
          boxs[nz][x][y] = boxs[z][x][y] + 1
          queue.append((nz, x, y))

    for c in range(4):
      nx = x + dx[c]
      ny = y + dy[c]

      if 0 <= nx < N and 0 <= ny < M:
        if boxs[z][nx][ny] == 0:
          boxs[z][nx][ny] = boxs[z][x][y] + 1
          queue.append((z, nx, ny))


  for h in range(H):
    for n in range(N):
      for m in range(M):
        if boxs[h][n][m] == 0:
          return -1
        ans = max(ans, boxs[h][n][m])

  return ans - 1


M, N, H = map(int, input().split())
boxs = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

dz = [-1, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())