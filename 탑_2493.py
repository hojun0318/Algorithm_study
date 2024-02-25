N = int(input())
tops = list(map(int, input().split()))
answer = []
stack = []

for i in range(N):
  while stack:
    if stack[-1][1] > tops[i]:
      answer.append(stack[-1][0] + 1)
      break
    else:
      stack.pop()

  if not stack:
    answer.append(0)
  
  stack.append([i, tops[i]])


print(*answer)
