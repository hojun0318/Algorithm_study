from collections import deque

M, N, H = map(int, input().split())
boxs = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()
ans = 0

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(H):
  for j in range(N):
    for k in range(M):
      if boxs[i][j][k] == 1:
        queue.append((i, j, k))

while queue:
  z, x, y = queue.popleft()

  for n in range(6):
    nx = x + dx[n]
    ny = y + dy[n]
    nz = z + dz[n]
    if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and boxs[nz][nx][ny] == 0 and boxs[nz][nx][ny] != -1:
      boxs[nz][nx][ny] = boxs[z][x][y] + 1
      queue.append((nz, nx, ny))

for a in boxs:
  for b in a:
    for c in b:
      if c == 0:
        print(-1)
        exit(0)
      ans = max(ans, c)

print(ans - 1)