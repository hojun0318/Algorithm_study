from collections import deque

def check(x, y):
  queue = deque()
  queue.append((x, y))
  
  while queue:
    x, y = queue.popleft()

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if 0 <= nx < N and 0 <= ny < M:
        if icebergs[nx][ny] != 0 and not visited[nx][ny]:
          visited[nx][ny] = 1
          queue.append((nx, ny))


def bfs():
  global year
  melt = 0
  melts = []
  queue = deque()
  len_queue = deque()

  for i in range(N):
    for j in range(M):
      if icebergs[i][j]:
        queue.append((i, j))
        len_queue.append((i, j))

  while queue:
    x, y = queue.popleft()

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if 0 <= nx < N and 0 <= ny < M:
        if icebergs[nx][ny] <= 0:
          melt += 1
    melts.append(melt)
    melt = 0

  for l in range(len(len_queue)):
    r = len_queue[l][0]
    c = len_queue[l][1]
    if icebergs[r][c] - melts[l] < 0:
      icebergs[r][c] = 0
    else:
      icebergs[r][c] -= melts[l]
  
  year += 1

N, M = map(int, input().split())
icebergs = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

year = 0

bfs()

while True:
  ice = 0
  visited = [[0] * M for _ in range(N)]
  
  for i in range(N):
    for j in range(M):
      if icebergs[i][j] and not visited[i][j]:
        ice += 1
        visited[i][j] = 1
        check(i, j)

  if ice == 0:
    print(0)
    break
  elif ice == 1:
    bfs()
  else:
    print(year)
    break