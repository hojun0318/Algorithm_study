from collections import deque

def bfs(x, y):
  queue = deque()
  bfs_visited = [[0] * 5 for _ in range(5)]
  queue.append((x, y))
  bfs_visited[x][y] = 1
  cnt = 1

  while queue:
    x, y = queue.popleft()

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if 0 <= nx < 5 and 0 <= ny < 5:
        if not bfs_visited[nx][ny] and visited[nx][ny] == 1:
          bfs_visited[nx][ny] = 1
          cnt += 1
          queue.append((nx, ny))

  if cnt == 7:
    return True


def check():
  for i in range(5):
    for j in range(5):
      if visited[i][j] == 1:
        return bfs(i, j)


def dfs(n, cnt, scnt):
  global ans
  
  if cnt > 7:
    return
  
  if n == 25:
    if cnt == 7 and scnt >= 4:
      if check():
        ans += 1
    return

  visited[n // 5][n % 5] = 1
  dfs(n + 1, cnt + 1, scnt + int(maps[n // 5][n % 5] == 'S'))
  visited[n // 5][n % 5] = 0

  dfs(n + 1, cnt, scnt)


maps = [list(map(str, input())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0, 0)

print(ans)