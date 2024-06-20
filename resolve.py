# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs():
  queue = deque()

  for x in range(R):
    for y in range(C):
      if load[x][y] == 'F':
        fire_visited[x][y] = 1
        queue.append((x, y, 'f'))

  for r in range(R):
    for c in range(C):
      if load[r][c] == 'J':
        jihun_visited[r][c] = 1
        queue.append((r, c, 'j'))

  while queue:
    x, y, s = queue.popleft()
    if s == 'j':
      if x == (R - 1) or x == 0 or y == 0 or y ==(C - 1):
        return jihun_visited[x][y]
      
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if s == 'j':
        if 0 <= nx < R and 0 <= ny < C:
          if load[nx][ny] == '.':
            if not jihun_visited[nx][ny] and not fire_visited[nx][ny]:
              jihun_visited[nx][ny] = jihun_visited[x][y] + 1
              queue.append((nx, ny, 'j'))

      if s == 'f':
        if 0 <= nx < R and 0 <= ny < C:
          if load[nx][ny] == '.' or load[nx][ny] == 'J':
            if not fire_visited[nx][ny]:
              fire_visited[nx][ny] = fire_visited[x][y] + 1
              queue.append((nx, ny, 'f'))

  return "IMPOSSIBLE"


R, C = map(int, input().split())
load = [list(map(str, input())) for _ in range(R)]
jihun_visited = [[0] * C for _ in range(R)]
fire_visited = [[0] * C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


print(bfs())


for i in fire_visited:
  print(i)
print('-----------------')
for i in jihun_visited:
  print(i)