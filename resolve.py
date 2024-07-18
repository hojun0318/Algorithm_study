from collections import deque

def bfs(tlst):
  queue = deque()
  visited = [[0] * (M + 2) for _ in range(N + 2)]
  cnt = 0

  for i in range(TC):
    if tlst[i] == 0:
      continue

    x, y = lst[i]
    queue.append((x, y))
    visited[x][y] = tlst[i]
  
  while queue:
    x, y = queue.popleft()
    if visited[x][y] == 25000:
      continue

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if seeds[nx][ny] == 0 or visited[nx][ny] == 25000:
        continue

      if visited[nx][ny] == 0:
        if visited[x][y] < 0:
          visited[nx][ny] = visited[x][y] - 1
          queue.append((nx, ny))
        else:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))

      else:
        if visited[x][y] < 0:
          if visited[nx][ny] + visited[x][y] - 1 == 0:
            cnt += 1
            visited[nx][ny] = 25000

        else:
          if visited[nx][ny] + visited[x][y] + 1 == 0:
            cnt += 1
            visited[nx][ny] = 25000

  return cnt


def dfs(n, gcnt, rcnt, tlst):
  global ans
  if n == TC:
    if gcnt == G and rcnt == R:
      ans = max(ans, bfs(tlst))
    return
  
  dfs(n + 1, gcnt + 1, rcnt,     tlst + [1])
  dfs(n + 1, gcnt,     rcnt + 1, tlst + [-1])
  dfs(n + 1, gcnt,     rcnt,     tlst + [0])



N, M, G, R = map(int, input().split())
seeds = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]
ans = 0
lst = []

for i in range(1, N + 1):
  for j in range(1, M + 1):
    if seeds[i][j] == 2:
      lst.append((i, j))

TC = len(lst)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0, 0, [])

print(ans)