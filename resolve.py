from collections import deque

def bfs():
  global ans
  queue = deque()
  visited = [[0] * (w + 2) for _ in range(h + 2)]

  for i in range(0, h + 2):
    for j in range(0, w + 2):
      if maps[i][j] == '.':
        if i == 0 or i == (h + 1) or j == 0 or j == (w + 1):
          visited[i][j] = 1
          queue.append((i, j))

  while queue:
    x, y = queue.popleft()

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      
      if 0 <= nx < (h + 2) and 0 <= ny < (w + 2):
        if maps[nx][ny] == '*':
          continue
      
        if not visited[nx][ny] and 'A' <= maps[nx][ny] <= 'Z':
          if maps[nx][ny].lower() not in keys:
            continue

        if maps[nx][ny] == '.' and not visited[nx][ny]:
          visited[nx][ny] = 1
          queue.append((nx, ny))

        elif maps[nx][ny] == '$':
          ans += 1
          maps[nx][ny] = '.'
          visited = [[0] * (w + 2) for _ in range(h + 2)]
          queue.append((nx, ny))

        elif not visited[nx][ny] and 'a' <= maps[nx][ny] <= 'z':
          if maps[nx][ny] not in keys:
            keys.append(maps[nx][ny])
            maps[nx][ny] = '.'
            visited = [[0] * (w + 2) for _ in range(h + 2)]
            queue.append((nx, ny))
          else:
            maps[nx][ny] = '.'
            visited = [[0] * (w + 2) for _ in range(h + 2)]
            queue.append((nx, ny))

        elif not visited[nx][ny] and 'A' <= maps[nx][ny] <= 'Z':
          if maps[nx][ny].lower() in keys:
            maps[nx][ny] = '.'
            queue.append((nx, ny))

  return ans


T = int(input())
for _ in range(T):
  h, w = map(int, input().split())
  maps = [['.'] * (w + 2)] + [['.'] + list(map(str, input())) + ['.'] for _ in range(h)] + [['.'] * (w + 2)]
  keys = []
  key = input()
  for i in range(len(key)):
    if key != '0':
      keys.append(key[i])
  
  ans = 0

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  print(bfs())