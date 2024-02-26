N = int(input())

nums = list(map(int, input().split()))
stk = []
ans = []

for i in range(len(nums)):
  while stk:
    if stk[-1] > nums[(N - 1) - i]:
      ans.append(stk[-1])
      stk.append(nums[(N - 1) - i])
      break
    else:
      stk.pop()

  if not stk:
    ans.append(-1)
  
  stk.append(nums[(N - 1) - i])

print(*ans[::-1])