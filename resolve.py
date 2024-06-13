def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  flag = 0
  for i in range(N):
    if visited[i] < M and flag != nums[i]:
      visited[i] += 1
      flag = nums[i]
      dfs(n + 1, lst + [nums[i]])
      visited[i] -= 1


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = []
visited = [0] * N

dfs(0, [])

for lst in ans:
  print(*lst)