def chk(i, j, s):
  if s == '<':
    if i > j:
      return False
  if s == '>':
    if i < j:
      return False
  
  return True


def dfs(n, num):
  if n == (k + 1):
    ans.append(num)
    return
  
  for i in range(10):
    if v[i] == 1:
      continue

    if n == 0 or chk(num[n - 1], str(i), ins[n - 1]):
      v[i] = 1
      dfs(n + 1, num + str(i))
      v[i] = 0


k = int(input())
ins = list(map(str, input().split()))
v = [0] * 10
ans = []

dfs(0, '')

ans.sort()

print(ans[-1])
print(ans[0])