from collections import deque

F, S, G, U, D = map(int, input().split())
# F : 총 층수 , S : 강호 층 , G : 스타트링크 층 , U : 위층 , : D : 아래층

cnt = [0 for _ in range(F + 1)]

flag = False

def bfs():
  global flag
  queue = deque()
  queue.append(S)
  cnt[S] = 1

  while queue:
    cur = queue.popleft()

    if cur == G:
      flag = True
      print(cnt[cur] - 1)
      break
    
    for i in (U, -D):
      nxt = cur + i

      if 1 <= nxt <= F and cnt[nxt] == 0:
        cnt[nxt] = cnt[cur] + 1
        queue.append(nxt)

bfs()

if flag == False:
  print('use the stairs')