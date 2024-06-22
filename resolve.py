# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]


      if 0 <= nx < N and 0 <= ny < N:
        if visited[nx][ny] == 0:
          visited[nx][ny] = 1
          queue.append((nx, ny))


N = int(input())
citys = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for h in range(101):
  visited = [[0] * N for _ in range(N)]
  cnt = 0
  for hi in range(N):
    for hj in range(N):
      if citys[hi][hj] <= h:
        visited[hi][hj] = 1

  for i in range(N):
    for j in range(N):
      if visited[i][j] == 0:
        visited[i][j] = 1
        cnt += 1
        bfs(i, j)

  ans = max(ans, cnt)

print(ans)