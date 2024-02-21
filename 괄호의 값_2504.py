str = input()

stack = []
ans = 0
cnt = 1

for i in range(len(str)):
  if str[i] == '(':
    stack.append(str[i])
    cnt *= 2

  elif str[i] == '[':
    stack.append(str[i])
    cnt *= 3

  elif str[i] == ')':
    if not stack or stack[-1] == '[':
      ans = 0
      break
    if str[i - 1] == '(':
      ans += cnt
    stack.pop()
    cnt //= 2

  elif str[i] == ']':
    if not stack or stack[-1] == '(':
      ans = 0
      break
    if str[i - 1] == '[':
      ans += cnt
    stack.pop()
    cnt //= 3

if stack:
  print(0)
else:
  print(ans)