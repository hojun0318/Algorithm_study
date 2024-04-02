while True:
  flag = True
  st = input()
  stk = []
  if st == '.':
    break

  for s in st:
    if s == '(':
      stk.append(s)
    if s == '[':
      stk.append(s)
    if s == ')':
      if stk :
        if stk[-1] == '(':
          stk.pop()
        elif stk[-1] == '[':
          flag = False
          break
      else:
        flag = False
        break
    if s == ']':
      if stk:
        if stk[-1] == '[':
          stk.pop()
        elif stk[-1] == '(':
          flag = False
          break
      else:
        flag = False
        break

  if stk or 0 == int(flag):
    print('no')
  else:
    print('yes')