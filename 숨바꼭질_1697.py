from collections import deque

N, K = map(int, input().split())

search = [0] * 100001

def bfs(s):
  queue = deque([s])
  while queue:
    s = queue.popleft()

    if s == K:
      return search[s]
    
    for ns in (s - 1, s + 1, s * 2):
      if 0 <= ns < 100001 and not search[ns]:
        search[ns] = search[s] + 1
        queue.append(ns)


print(bfs(N))