from collections import deque

T = int(input())

for _ in range(T):
  p = list(map(str, input()))
  n = int(input())
  lst = input().rstrip()[1:-1].split(",")
  
  if n != 0:
    queue = deque(lst)
  else:
    queue = deque([])

  flagError = False
  cnt = 0

  for c in p:
    if c == 'R':
      cnt += 1
    else:
      if len(queue) == 0:
        print('error')
        flagError = True
        break
      else:
        if cnt % 2 == 0:
          queue.popleft()
        else:
          queue.pop()

  if not flagError:
    if cnt % 2 == 0:
      print("[" + ",".join(queue) + "]")
    else:
      queue = deque(reversed(queue))
      print("[" + ",".join(queue) + "]")