from collections import deque

N, M = map(int, input().split())
icebergs = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

year = 0

def bfs():
  global year
  queue = deque()
  for i in range(N):
    for j in range(M):
      if icebergs[i][j]:
        queue.append((i, j))

  bfs_visited = [[0] * M for _ in range(N)]

  while queue:
    x, y = queue.popleft()
    bfs_visited[x][y] = 1

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if 0 <= nx < N and 0 <= ny < M:
        if icebergs[nx][ny] == 0 and not bfs_visited[nx][ny]:
          if icebergs[x][y] > 0:
            icebergs[x][y] -= 1
  
  year += 1

  new_queue = deque()
  visited = [[0] * M for _ in range(N)]
  cnt = 0

  for r in range(N):
    for c in range(M):
      if icebergs[r][c] and not visited[r][c]:
        new_queue.append((r, c))
        cnt += 1

        while new_queue:
          r, c = new_queue.popleft()

          for d in range(4):
            nr = r + dx[d]
            nc = c + dy[d]

            if 0 <= nr < N and 0 <= nc < M:
              if icebergs[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                new_queue.append((nr, nc))

  if cnt >= 2:
    print(year)
  else:
    if cnt == 0:
      print(0)
    else:
      bfs()

bfs()