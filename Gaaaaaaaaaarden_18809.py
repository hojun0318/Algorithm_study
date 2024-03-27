from collections import deque

def bfs(tlst):
  queue = deque()
  visited = [[0] * (M + 2) for _ in range(N + 2)]
  cnt = 0

  for i in range(TC):
    if tlst[i] == 0:
      continue

    ti, tj = lst[i]
    queue.append((ti, tj))
    visited[ti][tj] = tlst[i]

  while queue:
    ci, cj = queue.popleft()
    if visited[ci][cj] == 25000:
      continue

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      ni = ci + di
      nj = cj + dj

      if arr[ni][nj] == 0 or visited[ni][nj] == 25000:
        continue

      if visited[ni][nj] == 0:
        if visited[ci][cj] < 0:
          visited[ni][nj] = visited[ci][cj] - 1
          queue.append((ni, nj))
        else:
          visited[ni][nj] = visited[ci][cj] + 1
          queue.append((ni, nj))
      
      else:
        if visited[ci][cj] < 0:
          if visited[ni][nj] + visited[ci][cj] - 1 == 0:
            cnt += 1
            visited[ni][nj] = 25000
        else:
          if visited[ni][nj] + visited[ci][cj] + 1 == 0:
            cnt += 1
            visited[ni][nj] = 25000

  return cnt



def dfs(n, gcnt, rcnt, tlst):
  global ans
  if n == TC:
    if G == gcnt and R == rcnt:
      ans = max(ans, bfs(tlst))
    return
  
  dfs(n + 1, gcnt + 1, rcnt, tlst + [1])
  dfs(n + 1, gcnt, rcnt + 1, tlst + [-1])
  dfs(n + 1, gcnt, rcnt, tlst + [0])




N, M, G, R = map(int, input().split())
arr = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]

lst = []

for i in range(1, N + 1):
  for j in range(1, M + 1):
    if arr[i][j] == 2:
      lst.append((i, j))

TC = len(lst)

ans = 0
dfs(0, 0, 0, [])

print(ans)