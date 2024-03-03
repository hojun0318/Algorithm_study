from collections import deque

# L : 빌딩 층 수 , R : 한 층의 행 , C : 한 층의 열
# S : 시작점 , E : 도착점 , '#' : 벽 , '.' : 길

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

def bfs(z, x, y):
  queue = deque()
  queue.append((z, x, y))

  while queue:
    z, x, y = queue.popleft()

    if buildings[z][x][y] == 'E':
      return(f'Escaped in {visited[z][x][y] - 1} minute(s).')

    for l in range(6):
      nz = z + dz[l]
      nx = x + dx[l]
      ny = y + dy[l]

      if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
        if visited[nz][nx][ny] == 0 and buildings[nz][nx][ny] != '#':
          queue.append((nz, nx, ny))
          visited[nz][nx][ny] = visited[z][x][y] + 1

  return 'Trapped!'

while True:
  L, R, C = map(int, input().split())
  if L == 0 and R == 0 and C == 0:
    break
  buildings = []
  visited = [[[0] * C for _ in range(R)] for _ in range(L)]

  for _ in range(L):
    buildings.append([list(map(str, input())) for _ in range(R)])
    temp = input()

  for k in range(L):
    for i in range(R):
      for j in range(C):
        if buildings[k][i][j] == 'S':
          visited[k][i][j] = 1
          print(bfs(k, i, j))