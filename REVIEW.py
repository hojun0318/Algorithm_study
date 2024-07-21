def dfs(n, cnt):
  global ans

  if ans >= (cnt + (N - n) * 2):
    return

  if n == N:
    ans = max(ans, cnt)
    return
  
  if eggs[n][0] <= 0:
    dfs(n + 1, cnt)
  
  else:
    flag = False

    for i in range(N):
      if i == n or eggs[i][0] <= 0:
        continue

      flag = True
      eggs[n][0] -= eggs[i][1]
      eggs[i][0] -= eggs[n][1]

      dfs(n + 1, cnt + int(eggs[n][0] <= 0) + int(eggs[i][0] <= 0))

      eggs[n][0] += eggs[i][1]
      eggs[i][0] += eggs[n][1]
    
    if flag == False:
      dfs(n + 1, cnt)



N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dfs(0, 0)

print(ans)


#-----------------------------------------------------------------------


from collections import deque

def bfs(tlst):
  queue = deque()
  visited = [[0] * (M + 2) for _ in range(N + 2)]
  cnt = 0

  for i in range(TC):
    if tlst[i] == 0:
      continue

    tx, ty = lst[i]
    queue.append((tx, ty))
    visited[tx][ty] = tlst[i]
  
  while queue:
    x, y = queue.popleft()

    if visited[x][y] == ((N * M) + 1):
      continue

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if maps[nx][ny] == 0 or visited[nx][ny] == ((N * M) + 1):
        continue

      if visited[nx][ny] == 0:
        if visited[x][y] < 0:
          visited[nx][ny] = visited[x][y] - 1
          queue.append((nx, ny))
        else:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))

      else:
        if visited[x][y] < 0:
          if visited[nx][ny] + visited[x][y] - 1 == 0:
            cnt += 1
            visited[nx][ny] = ((N * M) + 1)

        else:
          if visited[nx][ny] + visited[x][y] + 1 == 0:
            cnt += 1
            visited[nx][ny] = ((N * M) + 1)

  return cnt



def dfs(n, gcnt, rcnt, tlst):
  global ans
  if n == TC:
    if gcnt == G and rcnt == R:
      ans = max(ans, bfs(tlst))
    return
  
  dfs(n + 1, gcnt + 1, rcnt,     tlst + [1])
  dfs(n + 1, gcnt,     rcnt + 1, tlst + [-1])
  dfs(n + 1, gcnt,     rcnt,     tlst + [0])



N, M, G, R = map(int, input().split())
maps = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]
ans = 0
lst = []

for i in range(1, N + 1):
  for j in range(1, M + 1):
    if maps[i][j] == 2:
      lst.append((i, j))

TC = len(lst)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0, 0, [])

print(ans)