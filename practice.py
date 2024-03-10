from collections import deque

N, M = map(int, input().split())

rooms = [[0] * N for _ in range(N)]
rooms[0][0] = 1

visited = [[0] * N for _ in range(N)]
visited[0][0] = 1

switch = []

ans = 0

for _ in range(M):
  x, y, a, b = map(int, input().split())
  switch.append([x, y, a, b])

queue = deque()
queue.append((0, 0))

da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]

while queue:
  tmp = []
  r, c = queue.popleft()

  for x, y, a, b in switch:
    if r == x - 1 and c == y - 1:
      rooms[a - 1][b - 1] = 1
        
      for i in range(4):
        na = (a - 1) + da[i]
        nb = (b - 1) + db[i]

        if 0 <= na < N and 0 <= nb < N:
          if visited[na][nb] == 1:
            queue.appendleft((a - 1, b - 1))
            visited[a - 1][b - 1] = 1

          if visited[na][b] == 0 and rooms[na][nb] == 1:
            tmp.append((na, nb))

  queue = tmp[:]




for room in rooms:
  for right in room:
    if right == 1:
      ans += 1

print(ans)