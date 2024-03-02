from collections import deque

N = int(input())
apart = [list(map(int, input())) for _ in range(N)]

cnt = 1
res = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n):
  global ans
  queue = deque()
  queue.append((x, y, n))
  apart[x][y] = n
  ans = 1

  while queue:
    x, y, n = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < N and apart[nx][ny] == 1:
        apart[nx][ny] = cnt
        queue.append((nx, ny, n))
        ans += 1

  return ans
        

for i in range(N):
  for j in range(N):
    if apart[i][j] == 1:
      ans = 0
      cnt += 1
      res.append(bfs(i, j, cnt))

print(cnt - 1)

res.sort()

for k in res:
  print(k)