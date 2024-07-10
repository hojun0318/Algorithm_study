def dfs(lst):
  global ans
  if sum(lst) == S:
    ans += 1
    return
  print(lst)
  for i in range(N):
    if not visited[i]:
      visited[i] = 1
      dfs(lst + [nums[i]])
      
      visited[i] = 0


N, S = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0] * N

ans = 0

dfs([])

print(ans)