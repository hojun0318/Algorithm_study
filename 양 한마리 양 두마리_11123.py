# import sys
# sys.setrecursionlimit(100000)

# def dfs(x, y):
#   if 0 <= x < H and 0 <= y < W:
#     if not visited[x][y] and maps[x][y] == '#':
#       visited[x][y] = 1
#       dfs(x - 1, y)
#       dfs(x, y - 1)
#       dfs(x + 1, y)
#       dfs(x, y + 1)
    
#       return True
  
#   return False

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < H and 0 <= ny < W:
        if not visited[nx][ny] and maps[nx][ny] == '#':
          visited[nx][ny] = 1
          queue.append((nx, ny))

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
  H, W = map(int, input().split())
  maps = [list(map(str, input())) for _ in range(H)]
  visited = [[0] * W for _ in range(H)]
  ans = 0

  for i in range(H):
    for j in range(W):
      # if maps[i][j] == '#':
      #   if dfs(i, j) == True:
      #     ans += 1

      if maps[i][j] == '#' and not visited[i][j]:
        bfs(i, j)
        ans += 1

  print(ans)