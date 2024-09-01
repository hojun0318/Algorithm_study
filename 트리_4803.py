from collections import deque

def bfs(s):
  flag = False
  queue = deque()
  queue.append((s))

  while queue:
    start = queue.popleft()

    if visited[start]:
      flag = True

    visited[start] = 1

    for node in graph[start]:
      if node == start:
        flag = True
      if not visited[node]:
        queue.append((node))

  return flag


TC = 1

while True:
  N, M = map(int, input().split())

  if N == 0 and M == 0:
    break
  
  graph = [[] for _ in range(N + 1)]
  visited = [0] * (N + 1)
  ans = 0

  for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

  for i in range(1, N + 1):
    if not visited[i]:
      if not bfs(i):
        ans += 1

  if ans == 0:
    print(f"Case {TC}: No trees.")
  elif ans == 1:
    print(f"Case {TC}: There is one tree.")
  else:
    print(f"Case {TC}: A forest of {ans} trees.")

  TC += 1