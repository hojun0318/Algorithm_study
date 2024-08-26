from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    cnt = 0

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < (R + 2) and 0 <= ny < (C + 2):
        if grid[nx][ny] == '.':
          cnt += 1

    if cnt < 3:
      new_grid[x][y] = 'X'


R, C = map(int, input().split())
grid = [['.'] * (C + 2)] + [['.'] + list(map(str, input())) + ['.'] for _ in range(R)] + [['.'] * (C + 2)]
new_grid = [['.'] * (C + 2) for _ in range(R + 2)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(R + 2):
  for j in range(C + 2):
    if grid[i][j] == 'X':
      bfs(i, j)

x_lst = []
y_lst = []

for i in range(R + 2):
  for j in range(C + 2):
    if new_grid[i][j] == 'X':
      x_lst.append(i)
      y_lst.append(j)

x_lst.sort()
y_lst.sort()

for x in range(x_lst[0], x_lst[-1] + 1):
  for y in range(y_lst[0], y_lst[-1] + 1):
    print(new_grid[x][y], end = '')
  print()