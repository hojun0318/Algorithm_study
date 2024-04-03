sticks = list(map(str, input()))

stk = []
ans = 0

for i in range(len(sticks)):
  if sticks[i] == '(':
    stk.append(sticks[i])
  elif sticks[i] == ')' and stk[-1] == '(':
    stk.pop()
    if sticks[i - 1] == ')':
      ans += 1
    else:
      ans += len(stk)
      
print(ans)