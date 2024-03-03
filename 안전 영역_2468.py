from collections import deque

N = int(input())
buildings = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y= queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if visited[nx][ny] == 0:
          queue.append((nx, ny))
          visited[nx][ny] = 1



for h in range(0, 100):
  cnt = 0
  visited = [[0] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if buildings[i][j] <= h:
        visited[i][j] = 1

  for r in range(N):
    for c in range(N):
      if buildings[r][c] > h and visited[r][c] == 0:
        visited[r][c] = 1
        bfs(r, c)
        cnt += 1
      ans = max(ans, cnt)

print(ans)