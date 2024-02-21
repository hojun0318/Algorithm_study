N = int(input())
temp = []
ans = []
for _ in range(N):
  lst = list(input().split())
  if lst[0] == 'push':
    temp.append(int(lst[1]))
  elif lst[0] == 'top':
    if temp:
      ans.append(temp[-1])
    else:
      ans.append(-1)
  elif lst[0] == 'size':
    ans.append(len(temp))
  elif lst[0] == 'empty':
    if temp:
      ans.append(0)
    else:
      ans.append(1)
  elif lst[0] == 'pop':
    if temp:
      ans.append(temp.pop())
    else:
      ans.append(-1)

for i in ans:
  print(i)