from collections import deque

N, M = map(int, input().split())
icebergs = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
  for j in range(M):
    if icebergs[i][j]:
      queue.append((i, j))

cnt = 0
flag = True

while queue:
  next = []
  melts = []

  # 녹는 양 계산
  for x, y in queue:
    melt = 0

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and icebergs[nx][ny] <= 0:
        melt += 1
    melts.append(melt)

  for k in range(len(queue)):
    r = queue[k][0]
    c = queue[k][1]
    icebergs[r][c] -= melts[k]

    if icebergs[r][c] > 0:
      next.append((r, c))

  # 빙하가 남은 위치 다시 큐에 삽입
  queue = next[:]

  if not next:
    break

  ice = deque([next[0]])
  ice_cnt = 1
  visited = [[0] * M for _ in range(N)]
  visited[next[0][0]][next[0][1]] = 1

  while ice:
    x, y = ice.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and icebergs[nx][ny] > 0 and not visited[nx][ny]:
        visited[nx][ny] = 1
        ice.append((nx, ny))
        ice_cnt += 1
  
  # 소요 기간 계산
  cnt += 1

  if ice_cnt != len(queue):
    flag = False
    break

if flag:
  print(0)
else:
  print(cnt)