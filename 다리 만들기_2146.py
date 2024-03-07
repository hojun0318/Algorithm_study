from collections import deque

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

num = cnt = 0
ans = 100001

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  maps[x][y] = cnt
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 1 and not visited[nx][ny]:
        maps[nx][ny] = cnt
        queue.append((nx, ny))
        visited[nx][ny] = 1


def load_bfs(v):
  queue = deque()
  visited = [[-1] * N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if maps[i][j] == v:
        visited[i][j] = 0
        queue.append((i, j))
  
  while queue:
    x, y = queue.popleft()

    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      if 0 <= nx < N and 0 <= ny < N:
        if maps[nx][ny] and maps[nx][ny] != v:
          return visited[x][y]
        if not maps[nx][ny] and visited[nx][ny] == -1:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))
  
  return 10001


for i in range(N):
  for j in range(N):
    if maps[i][j] == 1 and not visited[i][j]:
      cnt += 1
      num += 1
      bfs(i, j)

for v in range(1, (num + 1)):
  ans = min(ans, load_bfs(v))

print(ans)