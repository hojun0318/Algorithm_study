N = int(input())
tops = list(map(int, input().split()))
ans = []
stk = []

for i in range(N):
  while stk:
    if stk[-1][1] >= tops[i]:
      ans.append(stk[-1][0] + 1)
      break
    else:
      stk.pop()

  if not stk:
    ans.append(0)
  
  stk.append([i, tops[i]])

print(*ans)