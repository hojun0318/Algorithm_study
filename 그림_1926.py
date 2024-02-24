from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = cnt = ans = 0

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  global k
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    arr[x][y] = 0

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if arr[nx][ny] == 0:
        continue
      if arr[nx][ny] == 1:
        arr[nx][ny] = 0
        queue.append((nx, ny))
        k += 1

  return k


for i in range(N):
  for j in range(M):
    if arr[i][j] == 1:
      k = 1
      ans += 1
      cnt = bfs(i, j)
      if cnt > res:
        res = cnt

print(ans)
print(res)