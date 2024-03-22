def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  for i in range(N):
    if not lst:
      if visited[i] != M:
        visited[i] += 1
        dfs(n + 1, lst + [arr[i]])
        visited[i] -= 1
    else:
      if visited[i] != M and lst[-1] <= arr[i]:
        visited[i] += 1
        dfs(n + 1, lst + [arr[i]])
        visited[i] -= 1


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * (N + 1)
ans = []

dfs(0, [])

for lst in ans:
  print(*lst)