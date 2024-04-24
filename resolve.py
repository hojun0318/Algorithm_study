from collections import deque, defaultdict

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

def bfs():
  global ans, visited
  queue = deque()
  queue.append((0, 0))
  visited[0][0] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < h + 2 and 0 <= ny < w + 2 and not visited[nx][ny]:
        if buildings[nx][ny] == '*':
          continue

        if 'A' <= buildings[nx][ny] <= 'Z':
          if buildings[nx][ny].lower() not in keys:
            continue
            
        elif 'a' <= buildings[nx][ny] <= 'z':
            if buildings[nx][ny] not in keys:
              keys[buildings[nx][ny]] = buildings[nx][ny].upper()
              visited = [[0] * (w + 2) for _ in range(h + 2)]

        elif buildings[nx][ny] == '$' and (nx, ny) not in visited_document:
          ans += 1
          visited_document.append((nx, ny))

        visited[nx][ny] = 1
        queue.append((nx, ny))

  return ans

for _ in range(1, T + 1):
  h, w = map(int, input().split())
  buildings = [['.'] + list(map(str, input())) + ['.'] for _ in range(h)]
  buildings = [['.'] * (w + 2)] + buildings + [['.'] * (w + 2)]
  visited = [[0] * (w + 2) for _ in range(h + 2)]
  keys = defaultdict(int)
  visited_document = []
  ans = 0

  for key in input():
    if key.isalpha():
      keys[key] = key.upper()

  print(bfs())