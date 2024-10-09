from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  cnt = 1
  maps[x][y] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if maps[nx][ny] == 0:
          cnt += 1
          maps[nx][ny] = 1
          queue.append((nx, ny))

  return cnt


N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
lst = []
original_M = M

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
  for j in range(N):
    if maps[i][j] == 0:
      lst.append(bfs(i, j))

for num in lst:
  if num % K == 0:
    M = M - (num // K)
  else:
    M = M - (num // K) - 1

if original_M != M and M >= 0:
  print('POSSIBLE')
  print(M)
else:
  print('IMPOSSIBLE')