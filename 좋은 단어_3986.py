N = int(input())

ans = 0

for _ in range(N):
  str = input()
  stack = []
  stack.append(str[0])

  for s in range(1, len(str)):
    if stack and str[s] == stack[-1]:
      stack.pop()
    else:
      stack.append(str[s])

  if not stack:
    ans += 1
    
print(ans)