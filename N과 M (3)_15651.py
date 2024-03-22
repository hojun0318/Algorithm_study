def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  for i in range(1, N + 1):
    if visited1[i] != N:
      visited1[i] += 1
      dfs(n + 1, lst + [i])
      visited1[i] -= 1



N, M = map(int, input().split())
visited1 = [0] * (N + 1)

ans = []

dfs(0, [])

for lst in ans:
  print(*lst)