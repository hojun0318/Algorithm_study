def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  for i in range(1, N + 1):
    if not lst:
      if visited[i] != M:
        visited[i] += 1
        dfs(n + 1, lst + [i])
        visited[i] -= 1
    else:
      if visited[i] != M:
        if lst[-1] <= i:
          visited[i] += 1
          dfs(n + 1, lst + [i])
          visited[i] -= 1



N, M = map(int, input().split())
visited = [0] * (N + 1)
ans = []

dfs(0, [])

for lst in ans:
  print(*lst)