def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  prev = 0
  for i in range(N):
    if visited[i] == 0 and prev != arr[i]:
      prev = arr[i]
      visited[i] = 1
      dfs(n + 1, lst + [arr[i]])
      visited[i] = 0

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

visited = [0] * N
ans = []

dfs(0, [])

for lst in ans:
  print(*lst)