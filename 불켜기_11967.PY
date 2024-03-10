from collections import deque, defaultdict

N, M = map(int, input().split())

visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
lights = [[0] * N for _ in range(N)]
lights[0][0] = 1

switch = defaultdict(list)

for _ in range(M):
  x, y, a, b = map(int, input().split())
  switch[(x - 1, y - 1)].append((a - 1, b - 1))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
  res = 1
  queue = deque([(0, 0)])

  while queue:
    r, c = queue.popleft()
    for tr, tc in switch[(r, c)]:
      if not lights[tr][tc]:
        lights[tr][tc] = 1
        res += 1

        for i in range(4):
          nr = tr + dr[i]
          nc = tc + dc[i]

          if 0 <= nr < N and 0 <= nc < N:
            if visited[nr][nc]:
              queue.append((nr, nc))

    for j in range(4):
      nr = r + dr[j]
      nc = c + dc[j]
      if 0 <= nr < N and 0 <= nc < N:
        if not visited[nr][nc] and lights[nr][nc] == 1:
          queue.append((nr, nc))
          visited[nr][nc] = 1

  return res

print(bfs())