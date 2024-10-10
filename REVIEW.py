from collections import deque

def bfs(x, y, c):
  queue = deque()
  queue.append((x, y, c))
  visited[x][y] = 1

  while queue:
    x, y, c = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:
        if not visited[nx][ny] and maps[nx][ny] == c:
          if c == 'G':
            maps[nx][ny] = 'R'
          visited[nx][ny] = 1
          queue.append((nx, ny, c))


N = int(input())
maps = [list(map(str, input())) for _ in range(N)]
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(2):
  cnt = 0
  visited = [[0] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if maps[i][j] == 'R' and not visited[i][j]:
        cnt += 1
        bfs(i, j, 'R')
      if maps[i][j] == 'B' and not visited[i][j]:
        cnt += 1
        bfs(i, j, 'B')
      if maps[i][j] == 'G' and not visited[i][j]:
        cnt += 1
        maps[i][j] = 'R'
        bfs(i, j, 'G')

  ans.append(cnt)

print(*ans)