from collections import deque

N, M, K = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[K + 1 for _ in range(M)] for _ in range(N)]
visited[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
  queue = deque()
  queue.append(start)
  ans = 1
  time = True

  while queue:
    for _ in range(len(queue)):
      x, y, k = queue.popleft()

      if x == (N - 1) and y == (M - 1):
        print(ans)
        return
      
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] > k:
          if matrix[nx][ny] == 0:
            queue.append((nx, ny, k))
            visited[nx][ny] = k
          elif k < K:
            if not time: 
              queue.append((x, y, k))
            else: 
              visited[nx][ny] = k
              queue.append((nx, ny, k + 1))

    ans += 1
    time = not time

  print(-1)
  return

bfs((0, 0, 0))