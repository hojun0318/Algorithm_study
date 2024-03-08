from collections import deque

N, K = map(int, input().split())

visited = [0] * 100001
node = [0] * 100001

def path(x):
  lst = []
  tmp = x
  for _ in range(visited[x] + 1):
    lst.append(tmp)
    tmp = node[tmp]
  print(' '.join(map(str, lst[::-1])))

def bfs():
  queue = deque()
  queue.append(N)

  while queue:
    s = queue.popleft()

    if s == K:
      print(visited[s])
      path(s)
      return s
  
    for ns in (s - 1, s + 1, s * 2):
      if 0 <= ns < 100001 and not visited[ns]:
        visited[ns] = visited[s] + 1
        queue.append(ns)
        node[ns] = s


bfs()