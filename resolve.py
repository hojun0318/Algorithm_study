N = int(input())
buildings = []
for _ in range(N):
  buildings.append(int(input()))

stk = []
ans = 0

for i in buildings:
  while stk and stk[-1] <= i:
    stk.pop()
    
  stk.append(i)

  ans += len(stk) - 1

print(ans)