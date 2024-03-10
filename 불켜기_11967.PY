from collections import deque

N, M = map(int, input().split())

rooms = [[0] * N for _ in range(N)]
rooms[0][0] = 1
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1

switch = []

for _ in range(M):
  x, y, a, b = map(int, input().split())
  switch.append([x, y, a, b])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x, y):
  ans = 1
  queue = deque()
  queue.append((x, y))

  while queue:
    r, c = queue.popleft()

    for x, y, a, b in switch:
      if r == x - 1 and c == y - 1:
        if not rooms[a - 1][b - 1]:
          rooms[a - 1][b - 1] = 1
          ans += 1
        
          for i in range(4):
            nr = (a - 1) + dr[i]
            nc = (b - 1) + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
              if visited[nr][nc] == 1:
                queue.append((nr, nc))
      
    for j in range(4):
      nr = r + dr[j]
      nc = c + dc[j]

      if 0 <= nr < N and 0 <= nc < N:
        if rooms[nr][nc] == 1 and not visited[nr][nc]:
          queue.append((nr, nc))
          visited[nr][nc] = 1

  return ans

print(bfs(0, 0))