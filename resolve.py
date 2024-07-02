from collections import deque

def bfs(x, y):
  global ans
  now = deque()
  now.append((x, y))

  while now:
    x, y = now.popleft()

    if rooms[x][y]:
      
      queue = rooms[x][y]

      for a, b in queue:
        if not rights[a][b]:
          rights[a][b] = 1
          ans += 1

          for i in range(4):
            bx = a + dx[i]
            by = b + dy[i]

            if 0 <= bx < (N + 2) and 0 <= by < (N + 2):
              if visited[bx][by] == 1:
                now.append((bx, by))

    for j in range(4):
      nx = x + dx[j]
      ny = y + dy[j]

      if 0 <= nx < (N + 2) and 0 <= ny < (N + 2):
        if rights[nx][ny] == 1 and not visited[nx][ny]:
          visited[nx][ny] = 1
          now.append((nx, ny))

  return ans


N, M = map(int, input().split())
rooms = [[deque() for _ in range(N + 2)] for _ in range(N + 2)]
rights = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
visited = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

ans = 1

rights[1][1] = 1
visited[1][1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(M):
  x, y, a, b = map(int, input().split())
  rooms[x][y].append((a, b))


print(bfs(1, 1))