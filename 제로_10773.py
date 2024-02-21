K = int(input())
ans = []
for _ in range(K):
  num = int(input())
  if num > 0:
    ans.append(num)
  else:
    ans.pop()

res = 0
for i in ans:
  res += i

print(res)