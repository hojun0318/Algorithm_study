from collections import deque

N, M, P = map(int, input().split())
S = [0] + list(map(int,input().split()))
maps = [list(map(str, input())) for _ in range(N)]
castle = [deque() for _ in range(P + 1)]
ans = [0] * (P + 1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for p in range(1, P + 1):
  for i in range(N):
    for j in range(M):
      if maps[i][j] == str(p):
        castle[p].append((i, j))
        ans[p] += 1

print(castle)
print('-----------------------')

flag = True

while flag:
  flag = False
  
  for q in range(1, P + 1): # 1, 2
    if not castle[q]:
      continue
  
    queue = castle[q]
    print('queue : ', queue)
    print('-------')
    for _ in range(S[q]):
      if not q:
        break

      for _ in range(len(queue)):
        x, y = queue.popleft()
        print('x, y', x , y)

        for i in range(4):
          nx = x + (dx[i])
          ny = y + (dy[i])

          if 0 <= nx < N and 0 <= ny < M:
            if maps[nx][ny] == '.':
              maps[nx][ny] = str(q)
              for m in maps:
                print(m)
              print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
              ans[q] += 1
              queue.append((nx, ny))
              print('que : ', queue)
              flag = True

    print('큐 : ', queue)

print(*ans[1:])