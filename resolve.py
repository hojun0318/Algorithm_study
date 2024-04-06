from collections import deque

R, C = map(int, input().split())
maps = [list(map(str, input())) for _ in range(R)]

fire_visited = [[0] * C for _ in range(R)]
jihun_visited = [[0] * C for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def fire_bfs(x, y):
  fire_queue = deque()
  fire_queue.append((x, y))

  while fire_queue:
    x, y = fire_queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < R and 0 <= ny < C:
        if not fire_visited[nx][ny] and maps[nx][ny] != '#':
          fire_queue.append((nx, ny))
          fire_visited[nx][ny] = fire_visited[x][y] + 1

def jihun_bfs(x, y):
  jihun_queue = deque()
  jihun_queue.append((x, y))

  while jihun_queue:
    x, y = jihun_queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < R and 0 <= ny < C:
        if maps[nx][ny] != '#' and not jihun_visited[nx][ny]:
          if jihun_visited[x][y] + 1 < fire_visited[nx][ny] or not fire_visited[nx][ny]:
            jihun_queue.append((nx, ny))
            jihun_visited[nx][ny] = jihun_visited[x][y] + 1
      else:
        return jihun_visited[x][y]
        
  return "IMPOSSIBLE"


for i in range(R):
  for j in range(C):
    if maps[i][j] == 'F':
      fire_visited[i][j] = 1
      fire_bfs(i, j)
    if maps[i][j] == 'J':
      jihun_visited[i][j] = 1
      print(jihun_bfs(i, j))