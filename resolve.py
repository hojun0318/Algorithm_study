# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()
    if x == N - 1 and y == M - 1:
      return visited[N - 1][M - 1]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if not visited[nx][ny] and maps[nx][ny] == 1:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))
  
  return 0


N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))