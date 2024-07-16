def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  flag = 0
  for i in range(N):
    if lst:
      if lst[-1] <= nums[i] and not visited[i] and flag != nums[i]:
        flag = nums[i]
        visited[i] = 1
        dfs(n + 1, lst + [nums[i]])
        visited[i] = 0
    else:
      if not visited[i] and flag != nums[i]:
        flag = nums[i]
        visited[i] = 1
        dfs(n + 1, lst + [nums[i]])
        visited[i]  = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = []
visited = [0] * N

dfs(0, [])

for lst in ans:
  print(*lst)