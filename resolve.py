from collections import deque

N, M = map(int, input().split())
stk = list(map(int, input().split()))

queue = deque()
for i in range(1, N + 1):
  queue.append(i)

ans = 0

for num in stk:
  while True:
    if queue[0] == num:
      queue.popleft()
      break
    else:
      if queue.index(num) < len(queue) / 2:
        while queue[0] != num:
          queue.append(queue.popleft())
          ans += 1
      else:
        while queue[0] != num:
          queue.appendleft(queue.pop())
          ans += 1
          
print(ans)