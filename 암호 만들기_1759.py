def dfs(n, lst):
  if n == L:
    cnt1 = 0
    cnt2 = 0
    for st in lst:
      if st in ['a', 'e', 'i', 'o', 'u']:
        cnt1 += 1
      if st not in ['a', 'e', 'i', 'o', 'u']:
        cnt2 += 1

    if cnt1 > 0 and cnt2 > 1:
      ans.append(lst)
    return
  
  for i in range(C):
    if not lst:
      if visited[i] == 0:
        visited[i] = 1
        dfs(n + 1, lst + [arr[i]])
        visited[i] = 0
    else:
      if visited[i] == 0:
        if lst[-1] < arr[i]:
          visited[i] = 1
          dfs(n + 1, lst + [arr[i]])
          visited[i] = 0

L, C = map(int, input().split())
arr = sorted(list(map(str, input().split())))

visited = [0] * C
ans = []

dfs(0, [])

for lst in ans:
  res = ''
  for s in lst:
    res += s
  print(res)