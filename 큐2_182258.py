from collections import deque

N = int(input())
queue = deque()
ans = []

for str in range(N):
  lst = list(input().split())
  if lst[0] == 'push':
    queue.append(int(lst[1]))
  elif lst[0] == 'pop':
    if queue:
      ans.append(queue.popleft())
    else:
      ans.append(-1)
  elif lst[0] == 'size':
    ans.append(len(queue))
  elif lst[0] == 'empty':
    if queue:
      ans.append(0)
    else:
      ans.append(1)
  elif lst[0] == 'front':
    if queue:
      ans.append(queue[0])
    else:
      ans.append(-1)
  elif lst[0] == 'back':
    if queue:
      ans.append(queue[-1])
    else:
      ans.append(-1)

for i in ans:
  print(i)