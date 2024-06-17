def dfs(n, lst):
  if n == M:
    ans.append(lst)
    return
  
  for i in range(N):
    if visited[i] < M:
      visited[i] += 1
      dfs(n + 1, lst +[nums[i]])
      visited[i] -= 1


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []
visited = [0] * N

dfs(0, [])

for lst in ans:
  print(*lst)
