from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * 1000001

queue = deque()
queue.append(S)
visited[S] = 1
flag = False

while queue:
  s = queue.popleft()

  if s == G:
    flag = True
    print(visited[s] - 1)
    break

  for ns in (s + U, s - D):
    if 1 <= ns <= F and not visited[ns]:
      visited[ns] = visited[s] + 1
      queue.append(ns)

if flag == False:
  print('use the stairs')