from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and area[nx][ny] == 1:
        queue.append((nx, ny))
        area[nx][ny] = 0

  return 1

T = int(input())
for test_case in range(T):
  M, N, K = map(int, input().split())
  area = [[0] * M for _ in range(N)]

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  for _ in range(K):
    y, x = map(int, input().split())
    area[x][y] = 1
  
  cnt = 0

  for i in range(N):
    for j in range(M):
      if area[i][j] == 1:
        cnt += bfs(i, j)

  print(cnt)