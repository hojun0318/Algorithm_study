# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs():
  ans = 0
  queue = deque()
  for i in range(N):
    for j in range(M):
      if boxs[i][j] == 1:
        queue.append((i, j))

  while queue:
    x, y = queue.popleft()

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if 0 <= nx < N and 0 <= ny < M:
        if boxs[nx][ny] == 0:
          queue.append((nx, ny))
          boxs[nx][ny] = boxs[x][y] + 1

  for lst in boxs:
    for chk in lst:
      if chk == 0:
        return -1
      ans = max(ans, chk)

  return ans - 1

M, N = map(int, input().split())
boxs = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())