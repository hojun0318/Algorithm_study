from collections import deque

def dfs(v):
  dfs_visited[v] = 1
  print(v, end = ' ')

  graph[v].sort()
  for i in graph[v]:
    if not dfs_visited[i]:
      dfs(i)


def bfs(start):
  queue = deque()
  queue.append(start)
  bfs_visited[start] = 1

  while queue:
    v = queue.popleft()
    print(v, end = ' ')

    graph[v].sort()
    for i in graph[v]:
      if not bfs_visited[i]:
        queue.append(i)
        bfs_visited[i] = 1


N, M, V = map(int, input().split())

graph = [[] for _ in range((N + 1))]

dfs_visited = [0] * (N + 1)
bfs_visited = [0] * (N + 1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(V)
print()
bfs(V)