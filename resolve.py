from collections import deque

def bfs(n):
  queue = deque()
  queue.append(n)
  visited[n] = 1

  while queue:
    n = queue.popleft()
    
    if n == K:
      return visited[n] - 1

    for i in range(3):
      if i == 0:
        nx = n * dn[i]
      else:
        nx = n + dn[i]
      
      if 0 <= nx < 100001 and not visited[nx]:
        if i == 0:
          visited[nx] = visited[n]
          queue.append(nx)
        else:
          visited[nx] = visited[n] + 1
          queue.append(nx)


N, K = map(int, input().split())
visited = [0] * 100001

dn = [2, -1, 1]

print(bfs(N))