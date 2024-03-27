from collections import deque

def bfs(tlst):
  global cnt
  queue = deque()
  v = [[0] * (M + 2) for _ in range(N + 2)]

  for i in range(TC):
    if tlst[i] == 0:
      continue
    ti, tj = lst[i]
    queue.append((ti, tj))
    v[ti][tj] = tlst[i]

    while queue:
      ci, cj = queue.popleft()
      
      if v[ci][cj] == 25000:
        continue

      for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj

        if arr[ni][nj] == 0 or v[ni][nj] == 25000:
          continue

        if v[ni][nj] == 0:
          if v[ci][cj] < 0:
            v[ni][nj] = v[ci][cj] - 1
            queue.append((ni, nj))
          else:
            v[ni][nj] = v[ci][cj] + 1
            queue.append((ni, nj))
        else:
          if v[ci][cj] < 0:
            if v[ni][nj] + v[ci][cj] - 1 == 0:
              




def dfs(n, rcnt, gcnt, tlst):
  global ans
  if n == TC:
    if rcnt == RC and gcnt == GC:
      ans = max(ans, bfs(tlst))
    return

  dfs(n + 1, rcnt + 1, gcnt, tlst + [-1])
  dfs(n + 1, rcnt, gcnt + 1, tlst + [1])
  dfs(n + 1, rcnt, gcnt, tlst + [0])





N, M, RC, GC = map(int, input().split())
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