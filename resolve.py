from collections import deque

def bfs():
  lst = []
  queue = deque()
  for p in range(1, P + 1):
    for n in range(N):
      for m in range(M):
        if maps[n][m] == str(p):
          queue.append((n, m, p, dis[p - 1]))

  while queue:
    x, y, p, s = queue.popleft()
    s -= 1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if maps[nx][ny] == '.' or maps[nx][ny] == str(p):
          maps[nx][ny] = p

          if s > 0:
            queue.appendleft((nx, ny, p, s))
          else:
            queue.append((nx, ny, p, dis[p - 1]))
        
        if maps[nx][ny] == p:
          if s > 0:
            queue.appendleft((nx, ny, p, s))


  for p in range(1, P + 1):
    cnt = 0
    for n in range(N):
      for m in range(M):
        if maps[n][m] == str(p) or maps[n][m] == p:
          cnt += 1

    lst.append(cnt)

  return lst

N, M, P = map(int, input().split())
dis = list(map(int, input().split()))
maps = [list(map(str, input())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(*bfs())


for m in maps:
  print(m)