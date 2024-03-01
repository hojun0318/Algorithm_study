from collections import deque

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]

for _ in range(K):
  sy, sx, ey, ex = map(int, input().split())
  row_s = M - ex
  row_e = M - sx
  for i in range(row_s, row_e):
    for j in range(sy, ey):
      arr[i][j] = 9

ans = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  global cnt
  queue = deque()
  queue.append((x, y))
  arr[x][y] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue
      if arr[nx][ny] == 9:
        continue
      if arr[nx][ny] == 0:
          arr[nx][ny] = arr[x][y] + 1
          queue.append((nx, ny))
          cnt += 1

  return cnt



for r in range(M):
  for c in range(N):
    if arr[r][c] == 0:
      cnt = 1
      ans.append(bfs(r, c))

ans.sort()
print(len(ans))
print(*ans)