# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(x, y):
  global tmp
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    tmp += 1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and art[nx][ny] == 1:
        visited[nx][ny] = 1
        queue.append((nx, ny))

  return tmp






n, m = map(int, input().split())
art = [list(map(int, input().split())) for _ in range(n)]
cnt = ans = tmp = 0 
visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  for j in range(m):
    if not visited[i][j] and art[i][j] == 1:
      visited[i][j] = 1
      cnt += 1
      ans = max(ans, bfs(i, j))
      tmp = 0

print(cnt)
print(ans)