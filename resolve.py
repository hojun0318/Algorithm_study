# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  maps[x][y] = 0

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < M and 0 <= ny < N:
        if maps[nx][ny] == 1:
          maps[nx][ny] = 0
          queue.append((nx, ny))




T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  maps = [[0] * N for _ in range(M)]

  for _ in range(K):
    x, y = map(int, input().split())
    maps[x][y] = 1

  ans = 0

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  for i in range(M):
    for j in range(N):
      if maps[i][j] == 1:
        ans += 1
        bfs(i, j)

  print(ans)