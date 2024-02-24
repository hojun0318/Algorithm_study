from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(N):
  for j in range(M):
    if arr[i][j] == 1:
      queue.append((i, j))

while queue:
  x, y = queue.popleft()

  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      continue
    if arr[nx][ny] == -1:
      continue
    if arr[nx][ny] == 0:
      arr[nx][ny] = arr[x][y] + 1
      queue.append((nx, ny))

for a in arr:
  for b in a:
    if b == 0:
      print(-1)
      exit(0)
    ans = max(ans, b)

print(ans - 1)