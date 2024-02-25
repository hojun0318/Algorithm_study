import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(R)]
# = 벽, . = 지나갈 수 있는 공간, J = 지훈이의 미로에서의 초기 위치(지나갈 수 있는 공간), F = 불이 난 공간

f_visited = [[0] * C for _ in range(R)]
h_visited = [[0] * C for _ in range(R)]

f_queue = deque()
h_queue = deque()

for r in range(R):
  for c in range(C):
    if arr[r][c] == 'F':
      f_queue.append((r, c))
      f_visited[r][c] = 1
    if arr[r][c] == 'J':
      h_queue.append((r, c))
      h_visited[r][c] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  while f_queue:
    x, y = f_queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < R and 0 <= ny < C:
        if not f_visited[nx][ny] and arr[nx][ny] != '#':
          f_visited[nx][ny] = f_visited[x][y] + 1
          f_queue.append((nx, ny))

  while h_queue:
    x, y = h_queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < R and 0 <= ny < C:
        if arr[nx][ny] != '#' and not h_visited[nx][ny]:
          if not f_visited[nx][ny] or f_visited[nx][ny] > h_visited[x][y] + 1:
            h_visited[nx][ny] = h_visited[x][y] + 1
            h_queue.append((nx, ny))
      else:
        return h_visited[x][y]
    
  return "IMPOSSIBLE" 


print(bfs())