from collections import deque

def bfs():
  queue = deque()
  queue.append(a - 1)
  visited[a - 1] = 0

  while queue:
    now = queue.popleft()

    for i in range(now, N, lst[now]):
      if visited[i] == -1:
        queue.append(i)
        visited[i] = visited[now] + 1
        if i == (b - 1):
          return visited[i]

    for i in range(now, -1, -lst[now]):
      if visited[i] == -1:
        queue.append(i)
        visited[i] = visited[now] + 1
        if i == (b - 1):
          return visited[i]

  return -1


N = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())
visited = [-1] * 100001


print(bfs())