from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  while fire_queue:
    fire_x, fire_y = fire_queue.popleft()

    for i in range(4):
      fire_nx = fire_x + dx[i]
      fire_ny = fire_y + dy[i]

      if 0 <= fire_nx < h and 0 <= fire_ny < w:
        if building[fire_nx][fire_ny] != '#' and not fire_visited[fire_nx][fire_ny]:
          fire_visited[fire_nx][fire_ny] = fire_visited[fire_x][fire_y] + 1
          fire_queue.append((fire_nx, fire_ny))


  while human_queue:
    human_x, human_y = human_queue.popleft()

    for i in range(4):
      human_nx = human_x + dx[i]
      human_ny = human_y + dy[i]

      if 0 <= human_nx < h and 0 <= human_ny < w:
        if building[human_nx][human_ny] != '#' and not human_visited[human_nx][human_ny]:
          if not fire_visited[human_nx][human_ny] or fire_visited[human_nx][human_ny] > human_visited[human_x][human_y] + 1:
            human_visited[human_nx][human_ny] = human_visited[human_x][human_y] + 1
            human_queue.append((human_nx, human_ny))
      else:
        return human_visited[human_x][human_y]
      
  return "IMPOSSIBLE"


T = int(input())
for test_case in range(T):
  w, h = map(int, input().split())
  building = [list(map(str, input())) for _ in range(h)]

  fire_visited = [[0] * w for _ in range(h)]
  human_visited = [[0] * w for _ in range(h)]

  fire_queue = deque()
  human_queue = deque()

  for i in range(h):
    for j in range(w):
      if building[i][j] == '*':
        fire_visited[i][j] = 1
        fire_queue.append((i, j))
      
      if building[i][j] == '@':
        human_visited[i][j] = 1
        human_queue.append((i, j))

  print(bfs())