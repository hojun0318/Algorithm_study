from collections import deque

def bfs(X, cnt):
  queue = deque()
  queue.append((X, cnt))

  while queue:
    x, cnt = queue.popleft()
    if cnt == K:
      city.append(x)

    for s in load[x]:
      if way[s] == 0:
        way[s] = cnt + 1
        queue.append((s, cnt + 1))

  return

N, M, K, X = map(int, input().split())
load = [[] for _ in range(N + 1)]
way = [0] * (N + 1)
city = []
for _ in range(M):
  n1, n2 = map(int, input().split())
  load[n1].append(n2)


bfs(X, 0)
city.sort()

if city:
  for node in city:
    print(node)
else:
  print(-1)