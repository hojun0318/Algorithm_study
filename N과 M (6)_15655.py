def dfs(n, lst):
  if n == M:
    lst = sorted(lst)
    if lst not in ans:
      ans.append(lst)
    return
  
  for i in range(N):
    if visited[i] == 0:
      visited[i] = 1
      dfs(n + 1, lst + [arr[i]])
      visited[i] = 0



N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * (N + 1)
ans = []

dfs(0, [])

for lst in ans:
  print(*lst)