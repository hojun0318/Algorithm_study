T = int(input())

for _ in range(T):
  lst = list(map(str, input()))
  flag = 0
  stk = []
  for i in lst:
    if i == '(':
      stk.append(i)
    elif stk and i == ')' and stk[-1] == '(':
      stk.pop()
    elif not stk and i == ')':
      flag = 1


  if flag == 0 and len(stk) == 0:
    print('YES')
  else:
    print('NO')