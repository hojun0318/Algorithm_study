# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs():
  queue = deque()
  queue.append(S)
  visited[S] = 1

  while queue:
    s = queue.popleft()
    if s > G and D == 0:
      continue

    if s == G:
      return visited[s] - 1
    
    for ns in [(s + U), (s - D)]:
      if 1 <= ns < (F + 1):
        if not visited[ns]:
          visited[ns] = visited[s] + 1
          queue.append((ns))

  return "use the stairs"


F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)

print(bfs())

print(visited)