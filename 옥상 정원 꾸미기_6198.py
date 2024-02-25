N = int(input())

buildings = []
for n in range(N):
  buildings.append(int(input()))


stack = []
ans = 0

for i in buildings:
  while stack and stack[-1] <= i:
    stack.pop()
  stack.append(i)

  ans += len(stack) - 1


print(ans)