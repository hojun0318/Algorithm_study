def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  for i in range(N):
    if not visited[i]:
      visited[i] = 1
      dfs(n + 1, lst + [nums[i]])
      visited[i] = 0


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []
visited = [0] * N

dfs(0, [])

for lst in ans:
  print(*lst)