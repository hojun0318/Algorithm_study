from collections import deque

def bfs():
  queue = deque()
  queue.append(a - 1)
  visited[a - 1] = 0

  while queue:
    now = queue.popleft()
    
    for i in range(now, N, lst[now]):
      if visited[i] == -1:
        visited[i] = visited[now] + 1
        queue.append(i)
        if i == (b - 1):
          return visited[i]
    
    for j in range(now, -1, -lst[now]):
      if visited[j] == -1:
        visited[j] = visited[now] + 1
        queue.append(j)
        if j == (b - 1):
          return visited[j]
        
  return -1


N = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())
visited = [-1] * 10000

print(bfs())