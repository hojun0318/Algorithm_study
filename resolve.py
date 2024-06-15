def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  prev = 0
  for i in range(N):
    if not visited[i] and prev != nums[i]:
      prev = nums[i]
      visited[i] = 1
      dfs(n + 1, lst + [nums[i]])
      visited[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * N
ans = []

dfs(0, [])

for lst in ans:
  print(*lst)